#导入模块
import socket
#实例化
sk=socket.socket()
#定义连接IP和port
ip_port=('192.168.2.193',9999)
#绑定IP和port
sk.bind(ip_port)
#最大连接数
sk.listen(5)
#进入循环接收数据
while True:
    #等待客户端连接
    conn,adress=sk.accept()
    #一直使用当前连接进行数据发送，直到结束标志出现
    while True:
        #打开文件等待数据写入   ab 可添加二进制模式
        with open("C:/Users\Joker\Desktop/file","ab") as f:
            #接收数据
            data=conn.recv(1024)
            if data==b'quit':
                break
            #写入文件
            f.write(data)
        # #接收完成标志
        # conn.send("success".encode())
    # print("文件接受完成")
#关闭连接
sk.close()