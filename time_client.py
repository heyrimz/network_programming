# time_client.py

import socket # socket 모듈을 불러온다.
import time

# TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost",5000)

# time.sleep(1)
sock.connect(address)  # 서버에 연결
while True:
    print("현재시각 : ", sock.recv(1024).decode())  # 수신 내용을 문자열로 변환하여 출력
