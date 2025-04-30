
# Validação de número inteiro
entrada = input("Digite um número inteiro: ")
if entrada.isdigit():
    numero = int(entrada)
    print("Número válido:", numero)
else:
    print("Erro: entrada inválida para inteiro.")

# Validação de número decimal
try:
    numero = float(input("Digite um número decimal: "))
    print("Número decimal válido:", numero)
except ValueError:
    print("Erro: valor inválido para float.")

# Interpretação de valor booleano
entrada = input("Você aceita os termos? (s/n): ").lower()
if entrada in ["s", "sim", "y", "yes"]:
    resposta = True
elif entrada in ["n", "nao", "não", "no"]:
    resposta = False
else:
    resposta = None
print("Valor interpretado:", resposta)

# Conversão segura de lista de inteiros
entrada = input("Digite números separados por espaço: ").split()
try:
    numeros = list(map(int, entrada))
    print("Lista convertida com sucesso:", numeros)
except ValueError:
    print("Erro: todos os itens devem ser números inteiros.")
