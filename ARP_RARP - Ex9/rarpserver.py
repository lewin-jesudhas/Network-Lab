#from typing import Optional
from twisted.internet import reactor,protocol
# from twisted.internet.interfaces import IAddress
# from twisted.internet.protocol import Protocol
class RARP_server(protocol.Protocol):
    def __init__(self,table):
        self.table=table
    def connectionMade(self):
        print("client connected")
    def dataReceived(self, data: bytes):
        m=data.decode()
        ip=self.table[m]
        if ip is not None:
            reply=f"the ip address is{ip}"
            self.transport.write(reply.encode())
        else:
            self.transport.write("not valid".encode())
class RARP_factory(protocol.Factory):
    def __init__(self,table):
        self.table=table
    def buildProtocol(self, addr):
        return RARP_server(self.table)#
table={}
table["00:11:22:33:44"]="10.10.10.1"
table["00:11:22:33:44:55"]="10.10.10.2"
f=RARP_factory(table)#
reactor.listenTCP(8076,f)
reactor.run()


        
