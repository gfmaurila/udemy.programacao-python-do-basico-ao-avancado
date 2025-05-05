# Script NAPALM para coletar informações
from napalm import get_network_driver

driver = get_network_driver("ios")
# device = driver("192.168.1.1", "admin", "admin")
# device.open()
# print(device.get_facts())
print("Simulação de conexão com NAPALM")