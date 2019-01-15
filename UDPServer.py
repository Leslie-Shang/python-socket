from socket import *
serverPort=10000
severSocket=socket(AF_INET,SOCK_DGRAM)
severSocket.bind(('',serverPort))
print("The server is ready to receive")
while True:
    message,clientAddress=severSocket.recvfrom(1024)
    modifiedMessage=message.decode('utf-8').upper()
    severSocket.sendto(modifiedMessage.encode(),clientAddress)
