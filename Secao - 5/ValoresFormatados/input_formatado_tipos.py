
from datetime import datetime

# Número inteiro formatado
entrada = input("Digite um número inteiro: ").replace(".", "").replace(",", "")
if entrada.isdigit():
    numero = int(entrada)
    print("Número inteiro válido:", numero)
else:
    print("Erro: entrada inválida para inteiro.")

# Número decimal (float) com vírgula ou ponto
entrada = input("Digite um valor decimal (ex: 1234,56 ou 1234.56): ").replace(",", ".")
try:
    valor = float(entrada)
    print("Valor float válido:", valor)
except ValueError:
    print("Erro: entrada inválida para float.")

# Entrada de data
entrada = input("Digite uma data (formato dd/mm/aaaa): ")
try:
    data = datetime.strptime(entrada, "%d/%m/%Y").date()
    print("Data válida:", data)
except ValueError:
    print("Erro: formato inválido. Use dd/mm/aaaa.")

# Entrada de data e hora
entrada = input("Digite data e hora (formato dd/mm/aaaa HH:MM): ")
try:
    dt = datetime.strptime(entrada, "%d/%m/%Y %H:%M")
    print("Data e hora válidas:", dt)
except ValueError:
    print("Erro: formato inválido. Use dd/mm/aaaa HH:MM.")
