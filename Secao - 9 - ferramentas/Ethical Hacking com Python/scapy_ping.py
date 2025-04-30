
# Ping com Scapy
from scapy.all import *
from scapy.layers.inet import IP, ICMP

resposta = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=2)
if resposta:
    print("Host está ativo:", resposta.src)
else:
    print("Sem resposta do host.")
