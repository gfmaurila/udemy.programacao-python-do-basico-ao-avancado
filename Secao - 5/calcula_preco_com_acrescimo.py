
# Programa que calcula 10% de acréscimo no valor do produto

try:
    valor = float(input("Digite o valor do produto: R$ "))
    acrescimo = valor * 0.10
    valor_final = valor + acrescimo

    print(f"Valor original: R$ {valor:.2f}")
    print(f"Acréscimo de 10%: R$ {acrescimo:.2f}")
    print(f"Valor final com acréscimo: R$ {valor_final:.2f}")
except ValueError:
    print("Erro: Digite um número válido.")
