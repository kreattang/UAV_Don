import socket,time


host = '127.0.0.1'
port = 9090

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect((host,port))

for i in range(10):
    sk.sendall(("你好，我是Client No.%d" %i).encode("utf8"))
    data = sk.recv(1024)
    print(data.decode('UTF-8', 'ignore'))
    time.sleep(2)
    i = i + 1
sk.close()