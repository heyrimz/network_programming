# time_sever.py

import socket # socket 모듈 불러온다
import time

# TCP 소켓 생성
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ('',5000) # '' = 임의 주소, 포트 번호 = 5000
s.bind(address) # 소켓과 주소 결합
s.listen(5) # 연결 대기, 5개 항목까지 수용

client, addr = s.accept() # 연결혀용 , (client socket, rem_addr) 반환

while True:
    # client, addr = s.accept() # 연결혀용 , (client socket, rem_addr) 반환
    print("Connection requested from", addr)
    if client:
        time.sleep(1)
        client.send(time.ctime(time.time()).encode()) # 현재 시간을 전송
    # client.close()