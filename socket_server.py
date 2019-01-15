import socket
sk=socket.socket()
ip_port=("127.0.0.1",9999)
sk.bind(ip_port)
sk.listen(5)
while True:
    print("正在进行等待接受数据。。。")
    conn,adress=sk.accept()
    msg="连接成功"
    conn.send(msg.encode())
    while True:
        data=conn.recv(1024)
        print(data.decode())
        if data==b'exit':
            break
        conn.send(data)
        conn.send("_______".encode())
    conn.close()