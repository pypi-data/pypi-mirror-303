'''
 2022 Bjoern Annighoefer
'''

from eoq3.config import Config, EOQ_DEFAULT_CONFIG
from eoq3.domain import Domain
from eoq3.domainwrappers import SerialDomain
from eoq3.command import Cmd, Err, Cmp
from eoq3.serializer import DesCmd, CreateSerializer
from eoq3.frame.frame import Frm, FRM_TYPE
from eoq3.error import EOQ_ERROR, EOQ_ERROR_RUNTIME, EOQ_ERROR_INVALID_VALUE, EOQ_ERROR_CODES, EOQ_ERROR_INVALID_TYPE

from ..util.interproc import ADMIN_COMMANDS, ADMIN_REPLIES, SerMsg, DesMsg

from threading import Thread,Semaphore,Lock,Event
from multiprocessing import Process, Queue
import queue # imported for using queue.Empty exception
from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory
from collections import deque

import asyncio
from ssl import SSLContext

#type checking
from typing import List, Deque, Callable, Dict, Any


### EOQ3 AUTOBAHN WS PROTOCOL ###

class Eoq3ServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        super().__init__()
        self.request = None #store the request information after a client connected

    def onConnect(self, request):
        self.request = request
        
    def onOpen(self):
        self.factory.controller.LogInfo("WS host: client connected: %s"%(self.request.peer))
        self.factory.controller.AddConnection(self)
    
    def onMessage(self, payload, isBinary):
        if not isBinary:
            frmStr = payload.decode('utf8')
            self.factory.controller.ForwardFrame(frmStr,self)
            
    def onClose(self, wasClean, code, reason):
        client = self.request.peer if self.request else 'unknown'
        self.factory.controller.LogInfo("WS host: client disconnected: %s (clean=%s, code=%s, reason=%s)"%(client,wasClean,code,reason))
        self.factory.controller.RemoveConnection(self)

### AUTOBAHN SERVER CLASS ###    
    
class AutobahnServerController:
    def __init__(self,inQueue:Queue, outQueue:Queue, adminInQueue:Queue, adminOutQueue:Queue, host: str, port:int, timeout:float, sslContextFactory:Callable[[],SSLContext], sslContextFactoryArgs:Dict[str,Any]):
        self.inQueue:Queue = inQueue
        self.outQueue:Queue = outQueue
        self.adminInQueue:Queue = adminInQueue
        self.adminOutQueue:Queue = adminOutQueue
        self.host:str = host
        self.port:int = port
        self.timeout:float = timeout
        self.sslContextFactory = sslContextFactory
        #internals 
        self.connectionNb:int = 0
        self.shallRun:bool = True
        self.connections:Dict[Eoq3ServerProtocol,str] = {}
        self.connectionsLut:Dict[str,Eoq3ServerProtocol] = {}
        self.factory = None
        self.loop = None
        self.coro = None
        self.server = None
        #create admin monitoring thread 
        self.adminThread = Thread(target=self.__AdminThread)
        self.adminThread.start()
        #create input polling thread
        self.inputThread = Thread(target=self.__InputThread)
        self.inputThread.start()
        # ssl?
        self.sslContext = None
        if(None != sslContextFactory):
            self.sslContext = sslContextFactory(sslContextFactoryArgs)
        #create websocket 
        self.factory = WebSocketServerFactory()
        self.factory.protocol = Eoq3ServerProtocol
        self.factory.controller = self #make the client accessible by protocol
        self.loop = asyncio.get_event_loop()
        self.coro = self.loop.create_server(self.factory, self.host, self.port, ssl=self.sslContext)
        self.server = self.loop.run_until_complete(self.coro)
        #inform that the server is ready
        self.adminOutQueue.put(SerMsg(ADMIN_REPLIES.READY,'1'))
        
    def Stop(self)->None:
        #print('Stopping Autobahn WS server...')
        self.shallRun = False
        for c in self.connections.keys():
            self.loop.call_soon_threadsafe(c.sendClose)
        if(self.server):
            self.server.close()
        if(self.loop):
            self.loop.stop()
        #self.adminThread.join()
        self.inputThread.join()
        #print('Autobahn WS server stopped.')
        
    def ForwardFrame(self,frmStr:str,connection:Eoq3ServerProtocol)->None:
        conId = self.connections[connection]
        msg = SerMsg(conId, frmStr)
        self.outQueue.put(msg)
        #print("Request (%s): %s"%(conId,msg))
        
    def AddConnection(self,connection:Eoq3ServerProtocol)->None:
        #await self.connectionNbLock.acquire()
        #no lock necessary, because async functions cannot be preempted everywhere
        conId = str(self.connectionNb)
        self.connectionNb += 1
        #self.connectionNbLock.release()
        #conId = int(hash(connection))
        self.connections[connection] = conId
        self.connectionsLut[conId] = connection
        self.LogInfo("ConId established: %s"%(conId))
        
    def RemoveConnection(self,connection:Eoq3ServerProtocol)->None:
        if(connection in self.connections):
            conId = self.connections[connection]
            self.adminOutQueue.put(SerMsg(ADMIN_REPLIES.DISCONNECT, conId)) 
            del self.connections[connection] 
            del self.connectionsLut[conId] 
            self.LogInfo("ConId removed: %s"%(conId))
        else:
            self.LogInfo("Unknown connection. Cannot removed.")
        
    def SendAdminReplay(self,reply:str)->None:
        self.adminOutQueue.put(reply)
        
    def LogInfo(self,text:str)->None:
        msg = SerMsg(ADMIN_REPLIES.INFO, text)
        self.SendAdminReplay(msg)
    
    def __AdminThread(self):
        while(self.shallRun):
            try:
                adminCmd = self.adminInQueue.get(timeout=self.timeout)
                if(ADMIN_COMMANDS.STOP == adminCmd):
                    self.Stop()
            except queue.Empty:
                pass #wait for next frame
            except Exception as e:
                print('WS admin in queue failed: %s'%(str(e)))
        pass
        
    def __InputThread(self):
        while(self.shallRun):
            try:
                msg = self.inQueue.get(timeout=self.timeout)
                (conId,frmStr) = DesMsg(msg)
                connection = self.connectionsLut[conId]
                #connection.sendMessage(frmStr.encode('utf8'), False) #this seems to become unstable and looses messages if many messages are send in a short time
                self.loop.call_soon_threadsafe(connection.sendMessage, frmStr.encode('utf8'), False) #map to asyncio loop: this seems to be stable even under high workload
                #print("Reply (%s): %s"%(conId,msg))
            except queue.Empty:
                pass #wait for next frame
            except KeyError as e:
                print('Autobahn controller received msg for closed connection %s: %s'%(conId,msg))
            except Exception as e:
                print('Autobahn controller input queue failed: %s (%s)'%(str(e),type(e).__name__))
        
### AUTOBAHN SERVER PROCESS ####   
    
def AutobahnServerProcess(inQueue:Queue, outQueue:Queue, adminInQueue:Queue, adminOutQueue:Queue, host: str, port:int, timeout:float, sslContextFactory:Callable[[],SSLContext], sslContextFactoryArgs:Dict[str,Any]):
    server = AutobahnServerController(inQueue, outQueue, adminInQueue, adminOutQueue, host, port, timeout, sslContextFactory, sslContextFactoryArgs)
    #enter asyncio loop forever
    loop = asyncio.get_event_loop()
    loop.run_forever()
    loop.close()
    

### MAIN CLASS ###

class AutobahnWsDomainHost():
    def __init__(self, domain:Domain, shallForwardSerializedCmds:bool=False, host:str='127.0.0.1', port:int=5141, sslContextFactory:Callable[[],SSLContext]=None, sslContextFactoryArgs:Dict[str,Any]={}, nWorkers:int = 1, config:Config=EOQ_DEFAULT_CONFIG):
        self.domain:Domain = domain
        if(shallForwardSerializedCmds and not isinstance(domain,SerialDomain)):
            raise EOQ_ERROR_INVALID_TYPE('Can only forward serial commands to SerialDomains.')
        self.shallForwardSerializedCmds = shallForwardSerializedCmds
        self.host:str = host
        self.port:int = port
        self.sslContextFactory:Callable[[],SSLContext] = sslContextFactory
        self.nWorkers = nWorkers
        self.config:Config = config
        self.remoteFrmSerializer = CreateSerializer(config.remoteFrmSerializer)
        self.remoteCmdSerializer = CreateSerializer(config.remoteCmdSerializer)
        #msg queue
        self.msgQueue:Deque[str] = deque()
        self.msgQueueueLock:Lock = Lock()
        self.msgSignal:Semaphore = Semaphore(0)
        #event management
        self.connections:Dict[str,List[str]] = {} #stores the session ids known per connection
        #internals ws related
        self.serverReadyEvent:Event = Event()
        #process communication primitives
        self.inQueue:Queue = Queue()
        self.outQueue:Queue = Queue()
        self.adminInQueue:Queue = Queue()
        self.adminOutQueue:Queue = Queue()
        #init the cmd handler
        self.CmdHandler = self.__HandleCmdNormal
        if(self.shallForwardSerializedCmds):
            self.CmdHandler = self.__HandleCmdSerial
        #create admin monitoring thread
        self.shallRun:bool = True 
        self.adminThread:Thread = Thread(target=self.__AdminThread)
        self.adminThread.start()
        #create input polling thread
        self.inputThread:Thread = Thread(target=self.__InputThread)
        self.inputThread.start()
        #create worker threads
        self.workers:List[Thread] = [Thread(target=self.__WorkerThread, args=(i,)) for i in range(self.nWorkers)]
        for w in self.workers:
            w.start()
        
        #start autobahn in a separate process because of asyncio
        self.autobahnProcess = Process(name="AsyncIO WS Server", target=AutobahnServerProcess, args=(self.outQueue, self.inQueue, self.adminOutQueue, self.adminInQueue, self.host, self.port, self.config.threadLoopTimeout, sslContextFactory, sslContextFactoryArgs))
        self.autobahnProcess.daemon = True
        self.autobahnProcess.start()
        
        isConnected = self.serverReadyEvent.wait(self.config.connectTimeout)
        if(not isConnected):
            self.Stop()
            raise EOQ_ERROR_RUNTIME('Failed to create host %s:%d'%(host,port))
        
    def Stop(self):
        '''Graceful shutdown
        '''
        self.shallRun = False
        self.adminOutQueue.put(ADMIN_COMMANDS.STOP)
        self.adminThread.join()
        self.inputThread.join()
        for w in self.workers:
            w.join()
            
        
    def __AdminThread(self):
        while(self.shallRun):
            try:
                adminReply = self.adminInQueue.get(timeout=self.config.threadLoopTimeout)
                (msgId,data) = DesMsg(adminReply)
                if(ADMIN_REPLIES.READY == msgId):
                    self.serverReadyEvent.set()
                elif(ADMIN_REPLIES.DISCONNECT == msgId):
                    conId = data
                    if(conId in self.connections):
                        del self.connections[conId]
                elif(ADMIN_REPLIES.INFO == msgId):
                    self.config.logger.Info(data)
            except queue.Empty:
                pass #wait for next frame
            except Exception as e:
                self.config.logger.Warn('Server admin queue failed: %s'%(str(e)))
        
    def __InputThread(self):
        while(self.shallRun):
            try:
                msg = self.inQueue.get(timeout=self.config.threadLoopTimeout)
                self.msgQueueueLock.acquire()
                self.msgQueue.appendleft(msg)
                self.msgQueueueLock.release()
                self.msgSignal.release()
            except queue.Empty:
                pass #wait for next frame
            except Exception as e:
                self.config.logger.Warn('WS host input queue return failed: %s (%s)'%(str(e),type(e).__name__))
                
    def __WorkerThread(self, n:int):
        while(self.shallRun):
            isNewMsg = self.msgSignal.acquire(timeout=self.config.threadLoopTimeout)
            if(isNewMsg):
                #print("Worker %d: got job"%(n))
                self.msgQueueueLock.acquire()
                msg = self.msgQueue.pop()
                self.msgQueueueLock.release()
                (conId,frmStr) = DesMsg(msg)
                frm = None
                #decode the frame
                try:
                    frm = self.remoteFrmSerializer.DesFrm(frmStr)
                except Exception as e:
                    self.config.logger.Warn('Worker thread invalid frame: %s'%(str(e)))
                #process the command
                try:
                    if(FRM_TYPE.CMD == frm.typ):
                        self.CmdHandler(frm,conId)
                    elif(FRM_TYPE.OBS == frm.typ):
                        self.__Observe(conId, frm.sid)
                    elif(FRM_TYPE.UBS == frm.typ):
                        self.__Unobserve(conId, frm.sid)
                    else:
                        raise EOQ_ERROR_INVALID_VALUE("Expected frame type CMD, but got: %s"%(frm.typ))
                except Exception as e:
                    msg = str(e)
                    self.config.logger.Warn('Worker thread failed: %s'%(msg))
                    res = Err(EOQ_ERROR_CODES.UNKNOWN,msg)
                    self.__SendResult([res], frm.uid, frm.sid, conId)
                    
    def __SendResult(self,resStr:str,resSer:str,uid:int,sid:str,conId:str):
        #resStr = self.remoteCmdSerializer.SerCmd(res)
        frm = Frm(FRM_TYPE.RES,uid,resSer,resStr,sid)
        frmStr = self.remoteFrmSerializer.SerFrm(frm)
        msg = SerMsg(conId, frmStr)
        self.outQueue.put(msg)
        
    def __SendEvents(self,evts:list,uid:int,sid:str,conId:str):
        evtCmd = Cmp(evts)
        evtsStr = self.remoteCmdSerializer.SerCmd(evtCmd)
        frm = Frm(FRM_TYPE.EVT,uid,self.remoteCmdSerializer.Name(),evtsStr,sid)
        frmStr = self.remoteFrmSerializer.SerFrm(frm)
        msg = SerMsg(conId, frmStr)
        self.outQueue.put(msg)
        
    def __OnDomainEvent(self, evts, context, source):
        sessionId = context #context equals the session id
        #find the connection for this session id
        for k,v in self.connections.items(): #TODO: backwards search has bad performance
            if(sessionId in v):
                conId = k
                self.__SendEvents(evts, 0, sessionId, conId)
                break #loop ends here
                
    def __Observe(self, conId:str, sessionId:str)->None:
        if(conId in self.connections):
            sessionIds = self.connections[conId]
            if(sessionId not in sessionIds):
                sessionIds.append(sessionId)
        else:
            #initialize new session ID list
            self.connections[conId] = [sessionId]
        self.domain.Observe(self.__OnDomainEvent, sessionId, sessionId)
            
    def __Unobserve(self, conId:str, sessionId:str)->None:
        if(conId in self.connections):
            sessionIds = self.connections[conId]
            if(sessionId in sessionIds):
                sessionIds.remove(sessionId)
            #if this was the last session id, remove the connection from the list.
            if(0 == len(sessionIds)):
                del self.connections[conId]
        self.domain.Unobserve(self.__OnDomainEvent, sessionId, sessionId)
        
    def __HandleCmdNormal(self, frm:Frm, conId:str):
        try:
            cmd = DesCmd(frm.ser,frm.dat)
            res = self.domain.RawDo(cmd, frm.sid, frm.roc)
        except EOQ_ERROR as e:
            res = Err(e.code,e.msg)
        except Exception as e:
            res = Err(EOQ_ERROR_CODES.UNKNOWN,str(e))
        resStr = self.remoteCmdSerializer.SerCmd(res)
        resSer = self.remoteCmdSerializer.Name()
        self.__SendResult(resStr, resSer, frm.uid, frm.sid, conId)
        
    def __HandleCmdSerial(self, frm:Frm, conId:str):
        try:
            (resStr,resSer) = self.domain.SerRawDo(frm.dat, frm.sid, frm.ser, frm.roc)
        except EOQ_ERROR as e:
            res = Err(e.code,e.msg)
            resStr = self.remoteCmdSerializer.SerCmd(res)
            resSer = self.remoteCmdSerializer.Name()
        except Exception as e:
            res = Err(EOQ_ERROR_CODES.UNKNOWN,str(e))
            resStr = self.remoteCmdSerializer.SerCmd(res)
            resSer = self.remoteCmdSerializer.Name()
        self.__SendResult(resStr, resSer, frm.uid, frm.sid, conId)
        
                        
        

        
        
