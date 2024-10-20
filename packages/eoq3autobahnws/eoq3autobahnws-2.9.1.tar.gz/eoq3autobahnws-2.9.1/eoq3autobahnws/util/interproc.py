'''
 2024 Bjoern Annighoefer
'''

### HELPER FUNCTIONS FOR INTERNAL COMMUNICATION ###        

class ADMIN_COMMANDS:
    STOP = 'STOP'
    
class ADMIN_REPLIES:
    READY = 'READY'
    DISCONNECT = 'DISCONNECT'
    ERROR = 'ERROR'
    INFO = 'INFO'

MSG_ID_SEPERATOR = '|'
        
def SerMsg(msgId:int,frmStr:str):
    return str(msgId) + MSG_ID_SEPERATOR + frmStr

def DesMsg(msg:str)->(str,str):
    i = msg.find(MSG_ID_SEPERATOR)
    msgId = msg[0:i]
    data = msg[i+1:]
    return (msgId,data)