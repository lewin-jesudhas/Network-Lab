#from typing import Optional
from twisted.internet import reactor,protocol
# from twisted.internet.interfaces import IAddress
# from twisted.internet.protocol import Protocol
class RARP_client(protocol.Protocol):
    def connectionMade(self):
        mac=input("enter mac address:")
        self.transport.write(mac.encode())
    def dataReceived(self, data: bytes):
        macdata=data.decode()
        if macdata is not None:
            print("mac addr:",macdata)
        else:
            print("invalid mac address")
class RARP_clientfactory(protocol.ClientFactory):#
    def buildProtocol(self, addr):
        return RARP_client()
    def clientConnectionlost(self):
        print('Connection lost')
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed')
        reactor.stop()

reactor.connectTCP('localhost',8076,RARP_clientfactory())
reactor.run()
