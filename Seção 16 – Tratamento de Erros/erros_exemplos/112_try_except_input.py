
# Try e Except com input
try:
    numero = int(input("Digite um número inteiro: "))
    print("Número dobrado:", numero * 2)
except ValueError:
    print("Erro: você digitou algo que não é número inteiro.")
