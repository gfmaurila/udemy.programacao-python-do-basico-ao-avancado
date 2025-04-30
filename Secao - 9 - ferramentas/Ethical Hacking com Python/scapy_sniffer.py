
# Sniffer simples com Scapy (CTRL+C para parar)
from scapy.all import *

def pacote_sniffado(pacote):
    print("Pacote capturado:", pacote.summary())

sniff(prn=pacote_sniffado, count=5)
