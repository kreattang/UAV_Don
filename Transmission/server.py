import socketserver

class myTCPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).decode('UTF-8', 'ignore').strip()
            if not self.data : break
            print(self.data)
            self.feedback_data =("回复\""+self.data+"\":\n\t你好，Please Takeoff").encode("utf8")
            self.request.sendall(self.feedback_data)

# host = '127.0.0.1'
host = input("IP:")
port = int(input("port:"))
server = socketserver.ThreadingTCPServer((host,port),myTCPhandler)
server.serve_forever()