import sys
from scapy.all import *

print(conf.ifaces)

# 패킷 캡처를 시작합니다.
# 인터페이스 이름을 실제로 사용하는 넽워크 인터페이스 이름으로 변경하세요.

while True:
    sniff(ifaces="Software Loopback Interface 1",prn = lambda x:x.show())
