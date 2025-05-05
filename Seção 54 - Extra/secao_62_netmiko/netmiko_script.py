# Script Netmiko para acesso a roteadores
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'admin'
}

# connection = ConnectHandler(**device)
# connection.send_command("show ip int brief")
print("Simulação de conexão com Netmiko")