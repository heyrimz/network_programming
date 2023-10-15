from socket import *
import _thread

HOST = 'localhost'
PORT = 2500
BUFF = 1024

def response(key):
    return '서버 응답 메세지'

def handler(clientsock, addr):
    while True:
        data = clientsock.recv(BUFF)
        print('data : ' + repr(data))
        if not data: break
        clientsock.send(response('').encode())
        print('sent : ' + repr(response('')))

if __name__ == '__main__':
    ADDR = (HOST,PORT)
    seversock = socket(AF_INET, SOCK_STREAM)
    seversock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    seversock.bind(ADDR)
    seversock.listen(5)

while True:
    print('waiting for connection...')
    clientsock, addr = seversock.accept()
    print('...connected from:', addr)
    _thread.start_new_thread(handler,(clientsock,addr))