
# Traceroute com Scapy
from scapy.all import *

print("Executando traceroute para 8.8.8.8:")
res, _ = traceroute("8.8.8.8", maxttl=10)
res.show()
