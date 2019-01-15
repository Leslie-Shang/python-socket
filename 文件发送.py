#导入模块
import socket
#实例化模块
sk=socket.socket()
#定义连接IP和port
ip_port=('127.0.0.1',9999)
#服务器连接
sk.connect(ip_port)
#文件上传
#打开文件
with open('D:/QQ/qq下载数据/1249571973/FileRecv/MobileFile/Image/1.png','rb') as f:
    #按每一段分割文件
    for i in f:
        #数据上传
        sk.send(i)
        # #等待接收完成标志
        # data=sk.recv(1024)
        # #判断服务器端是否真正的接收完成
        # if data!=b'success':
        #     break
#给服务器端发送结束信号
sk.send('quit'.encode())
