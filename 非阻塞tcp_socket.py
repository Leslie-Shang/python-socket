import socketserver
class myServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        conn=self.request
        msg="连接成功"
        conn.send(msg.encode())
        while True:
            data=conn.recv(1024)
            print(data.decode())
            if data==b'exit':
                break
            conn.send(data)
            conn.send("________".encode())
        conn.close()

    def finish(self):
        pass

if __name__=="__main__":
    server=socketserver.ThreadingTCPServer(("127.0.0.1",9999),myServer)
    server.serve_forever()