
# Exercício: Cálculo de Desconto
# Aplique desconto conforme valor da compra

valor = float(input("Digite o valor da compra: R$ "))

if valor > 200:
    desconto = valor * 0.10
elif valor > 100:
    desconto = valor * 0.05
else:
    desconto = 0

valor_final = valor - desconto
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
