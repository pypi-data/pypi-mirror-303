'''
 2022 Bjoern Annighoefer
'''

from eoq3.config import Config, EOQ_DEFAULT_CONFIG
from eoq3.domainwrappers import RemoteDomainClient
from eoq3.command import Cmd, IsReadOnlyCmd
from eoq3.error import EOQ_ERROR_RUNTIME

from ..util.interproc import ADMIN_COMMANDS, ADMIN_REPLIES, SerMsg, DesMsg

from threading import Thread,Event
from multiprocessing import Process, Queue
import queue # imported for using queue.Empty exception
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory

import asyncio
from ssl import SSLContext
#type checking
from typing import Dict, Callable, Any, Tuple



'''
 CLIENT
 
'''

class Eoq3ClientProtocol(WebSocketClientProtocol):

    def onOpen(self):
        self.factory.client.LogInfo("WS client: Connected to host: %s "%(self.peer))
        self.factory.client.SendAdminReplay(SerMsg(ADMIN_REPLIES.READY,'1'))
    
    def onMessage(self, payload, isBinary):
        if not isBinary:
            frmStr = payload.decode('utf8')
            self.factory.client.ForwardFrame(frmStr)
            
    def onClose(self, wasClean, code, reason):
        host = self.peer
        self.factory.client.LogInfo("WS client: Disconnected from host: %s (clean=%s, code=%s, reason=%s)"%(host,wasClean,code,reason))
        self.factory.client.SendAdminReplay(SerMsg(ADMIN_REPLIES.DISCONNECT,'1'))
    
    
class AutobahnClient:
    def __init__(self,inQueue:Queue, outQueue:Queue, adminInQueue:Queue, adminOutQueue:Queue, host: str, port:int, timeout:float, sslContextFactory:Callable[[],SSLContext], sslFactoryArgs:Dict[str,Any]):
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.adminInQueue = adminInQueue
        self.adminOutQueue = adminOutQueue
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sslContextFactory = sslContextFactory
        #internals 
        self.sslContext = None
        self.loop = None
        self.client = None
        self.ws = None
        self.shallRun:bool = True
        #create admin monitoring thread 
        self.adminThread = Thread(target=self.__AdminThread)
        self.adminThread.start()
        #create input polling thread
        self.inputThread = Thread(target=self.__InputThread)
        self.inputThread.start()
        #create websocket 
        if(None != sslContextFactory):
            self.sslContext = sslContextFactory(sslFactoryArgs)
        self.factory = WebSocketClientFactory()
        self.factory.protocol = Eoq3ClientProtocol
        self.factory.client = self #make the client accessible by protocol
        self.loop = asyncio.get_event_loop()
        self.coro = self.loop.create_connection(self.factory, self.host, self.port, ssl=self.sslContext)
        (transport, protocol) = self.loop.run_until_complete(self.coro)
        self.client = transport
        self.ws = protocol
        
    def Stop(self)->None:
        #print('Stopping Autobahn WS client...')
        self.shallRun = False
        if(self.ws):
            self.loop.call_soon_threadsafe(self.ws.sendClose)
        if(self.loop):
            self.loop.stop()
        #self.adminThread.join()
        self.inputThread.join()
        #print('Autobahn WS client stopped.')
        
    def ForwardFrame(self,frmStr:str)->None:
        self.outQueue.put(frmStr)
        
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
                frmStr = self.inQueue.get(timeout=self.timeout)
                self.loop.call_soon_threadsafe(self.ws.sendMessage, frmStr.encode('utf8'), False) #map to asyncio loop?
            except queue.Empty:
                pass #wait for next frame
            except Exception as e:
                print('Autobahn client input queue failed: %s (%s)'%(str(e),type(e).__name__))
        
    
    
def AutobahnProcess(inQueue:Queue, outQueue:Queue, adminInQueue:Queue, adminOutQueue:Queue, host: str, port:int, timeout:float, sslContextFactory:Callable[[],SSLContext], sslFactoryArgs:Dict[str,Any]):
    client = AutobahnClient(inQueue, outQueue, adminInQueue, adminOutQueue, host, port, timeout, sslContextFactory, sslFactoryArgs)
    #enter asyncio loop forever
    asyncio.get_event_loop().run_forever()
    

class AutobahnWsDomainClient(RemoteDomainClient):
    def __init__(self, host:str='127.0.0.1', port:int=5141, sslContextFactory:Callable[[],SSLContext]=None, sslFactoryArgs:Dict[str,Any]={}, config:Config=EOQ_DEFAULT_CONFIG, name:str="AutobahnWsDomainClient"):
        super().__init__(config,name)
        self.host:str = host
        self.port:int = port
        self.sslContextFactory:Callable[[],SSLContext] = sslContextFactory
        #internals ws related
        self.wsReadyEvent:Event = Event()
        #process communication primitives
        self.inQueue:Queue = Queue()
        self.outQueue:Queue = Queue()
        self.adminInQueue:Queue = Queue()
        self.adminOutQueue:Queue = Queue()
        #create admin monitoring thread
        self.shallRun:bool = True 
        self.adminThread:Thread = Thread(target=self.__AdminThread)
        self.adminThread.start()
        #create input polling thread
        self.inputThread:Thread = Thread(target=self.__InputThread)
        self.inputThread.start()
        #start autobahn in a separate process because of asyncio
        self.autobahnProcess:Process = Process(target=AutobahnProcess, args=(self.outQueue, self.inQueue, self.adminOutQueue, self.adminInQueue, self.host, self.port, self.config.threadLoopTimeout, sslContextFactory, sslFactoryArgs, ))
        self.autobahnProcess.daemon = True
        self.autobahnProcess.start()
        
        isConnected = self.wsReadyEvent.wait(timeout=self.config.connectTimeout)
        if(not isConnected):
            self.Close()
            raise EOQ_ERROR_RUNTIME('Could not connect to %s:%d'%(host,port))
            
        
    def __AdminThread(self):
        while(self.shallRun):
            try:
                adminReply = self.adminInQueue.get(timeout=self.config.threadLoopTimeout)
                (msgId,data) = DesMsg(adminReply)
                if(ADMIN_REPLIES.READY == msgId):
                    self.wsReadyEvent.set()
                elif(ADMIN_REPLIES.DISCONNECT == msgId):
                    self.wsReadyEvent.clear()
                elif(ADMIN_REPLIES.INFO == msgId):
                    self.config.logger.Info(data)
            except queue.Empty:
                pass #wait for next frame
            except Exception as e:
                self.config.logger.Error('Domain admin queue failed: %s'%(str(e)))
        pass
        
    def __InputThread(self):
        while(self.shallRun):
            try:
                frmStr = self.inQueue.get(timeout=self.config.threadLoopTimeout)
                self.OnSerFrmReceived(frmStr)
            except queue.Empty:
                pass #wait for next frame
            except Exception as e:
                self.config.logger.Error('WS client input queue failed: %s (%s)'%(str(e),type(e).__name__))
    
    #@Overrride
    def Close(self):
        self.shallRun = False
        self.adminOutQueue.put(ADMIN_COMMANDS.STOP)
        self.adminThread.join()
        self.inputThread.join()
        
    #@Override
    def SendSerFrm(self,frmStr:str)->None:
        '''Need to be implemented because it is called within RemoteDomainCLient
        '''
        self.outQueue.put(frmStr)
    
    #@Override
    def SerRawDo(self, cmdStr:str, sessionId:str=None, serType:str=None, readOnly:bool=False)->Tuple[str,str]:
        #check if the web socket is connected
#         isConnected = self.wsReadyEvent.wait(self.config.connectTimeout)
#         if(not isConnected):
#             raise EOQ_ERROR_RUNTIME("Send timeout: WS disconnected?")
        #if connected used the default behavior of serial domains
        (resStr,resSerType) = super().SerRawDo(cmdStr, sessionId, serType, readOnly)
        return (resStr,resSerType)
    
    def RawDo(self, cmd:Cmd, sessionId:str=None, readOnly:bool=None):
        #override readOnly, because it is essential for the server performance
        readOnly = IsReadOnlyCmd(cmd)
        return RemoteDomainClient.RawDo(self, cmd, sessionId=sessionId, readOnly=readOnly)
        
        
        
