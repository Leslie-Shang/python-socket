from socket import *
serverName=input("请输入主机IP：")
serverPort=10000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('输入英文字符串：')
clientSocket.sendto(message.encode('utf-8'),(serverName,serverPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(1024)
print(modifiedMessage.decode())
clientSocket.close()