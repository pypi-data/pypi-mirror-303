'''
 2022 Bjoern Annighoefer
'''

from eoq3.domainwrappers.remotedomainclient import RemoteDomainClient
from eoq3.config import Config, EOQ_DEFAULT_CONFIG
from eoq3.error import EOQ_ERROR_RUNTIME

import socket
import queue
from threading import Thread
import traceback


'''
 TCP DOMAIN CLIENT
 
'''


class ResultWaitInfo:
    def __init__(self,commandId,doStrategy:int,semaphore=None,callback=None):
        self.commandId = commandId
        self.doStrategy = doStrategy
        self.semaphore = semaphore
        self.callback = callback
        self.res = None #this can be used to transfare back the result to the sync thread
    


class TcpDomainClient(RemoteDomainClient):
    def __init__(self, host:str='localhost', port:int=6141, maxMsgSize:int=2**16 , msgSep:bytes=b'\x00', config:Config=EOQ_DEFAULT_CONFIG, name:str="TcpDomainClient"):
        super().__init__(config,name)
        self.host = host
        self.port = port
        self.maxMsgSize = maxMsgSize
        self.msgSep = msgSep #the separation sequence between two frames
        #internals
        self.shallRun = True
        #try to connect
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.config.connectTimeout)
        try:
            serverAddress = (self.host, self.port)
            self.socket.connect(serverAddress)
        except:
            raise EOQ_ERROR_RUNTIME("Could not connect to TCP server %s:%d"%(self.host,self.port))
        #start receiving thread
        self.rxThread = Thread(target=self.__RxThread, args=('TCP Client RxThread',))
        self.rxThread.start()
        #raw logging
        if(self.config.remoteRawLogging):
            self.rawSendLog = open("raw_send.txt", "w")
            self.rawRecvLog = open("raw_recv.txt", "w")
    
    #@Override    
    def Close(self):
        self.shallRun = False
        self.rxThread.join()
        self.socket.close()
        #raw logging
        if(self.config.remoteRawLogging):
            self.rawSendLog.close()
            self.rawRecvLog.close()
        
    #@Override
    def SendSerFrm(self,frmStr:str)->None:
        '''Need to be implemented because it is called within RemoteDomainClient
        '''
        msg = frmStr.encode("utf8")+self.msgSep
        self.socket.sendall(msg)
        if(self.config.remoteRawLogging):
            self.rawSendLog.write(frmStr+"\n")

    def __RxThread(self, name:str):
        msgQueue = queue.Queue()
        msgAccumulator = bytes()
        while(self.shallRun):
            try:
                data = self.socket.recv(self.maxMsgSize)
                if len(data)>0:
                    msgAccumulator += data

                    msgs = msgAccumulator.split(self.msgSep)
                    if len(msgAccumulator) >= len(self.msgSep) and \
                            msgAccumulator[len(msgAccumulator)-len(self.msgSep):len(msgAccumulator)-1] == self.msgSep:
                        for msg in msgs: msgQueue.put(msg.decode('utf-8'))
                    else:
                        for msg in msgs[:-1]: msgQueue.put(msg.decode('utf-8'))
                        msgAccumulator = msgs[-1]
                    
                    while not msgQueue.empty():
                        msg = msgQueue.get()
                        
                        if(self.config.remoteRawLogging):
                            self.rawRecvLog.write(msg+"\n")
                        try:
                            self.OnSerFrmReceived(msg)
                        except Exception as e:
                            print('%s: %s raw callback failed: %s'%(self,name,str(e)))
                            traceback.print_exc()
            except socket.timeout:
                pass #wait for next frame
            except socket.error as e:
                if e.errno == socket.errno.ECONNRESET:
                    # Handle disconnection -- close & reopen socket etc.
                    self.shallRun = False;
            except Exception as e:
                print('%s: %s failed: %s'%(self,name,str(e)))
                traceback.print_exc()
        #thread terminates here