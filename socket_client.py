import socket
client=socket.socket()
ip_port=("127.0.0.1",9999)
client.connect(ip_port)
while True:
    data=client.recv(1024)
    print(data.decode())
    msg=input("请输入要发送的消息：")
    client.send(msg.encode())
    if msg=='exit':
        break
    data = client.recv(1024)
    print(data.decode())

