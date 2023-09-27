import socket

s_sock = socket.socket()
host = "localhost"
prot = 2500

# 서버에 연결
s_sock.connect((host,prot))
s_sock.send("I am ready".encode())

fn = s_sock.recv(1024).decode() # 받았지만 차이를 위해 새로 지정

with open("./dummy/"+"recv","wb") as f:
    print("receiving")
    while True:
        data = s_sock.recv(1024)
        if not data:
            break
        f.write(data)

print("download complte")
s_sock.close()