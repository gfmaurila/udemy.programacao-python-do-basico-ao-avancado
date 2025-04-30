
# ----------- Exemplos de uso de input() -----------

# 1. Entrada simples de texto
nome = input("Digite seu nome: ")  # Usuário digita algo e é armazenado na variável 'nome'
print("Olá,", nome)

# 2. Entrada de número inteiro
idade = int(input("Digite sua idade: "))  # Converte a entrada de string para int
print("Você tem", idade, "anos.")

# 3. Entrada de número decimal
altura = float(input("Digite sua altura em metros: "))  # Converte para float
print("Sua altura é:", altura, "m")

# 4. Entrada e separação de múltiplos dados
entrada = input("Digite seu nome e idade separados por vírgula: ")  # Ex: Ana,30
nome2, idade2 = entrada.split(",")  # Divide a string em duas partes
print("Nome:", nome2)
print("Idade:", idade2)

# 5. Usando map() para converter múltiplos números
numeros = list(map(int, input("Digite 3 números separados por espaço: ").split()))
print("Números digitados:", numeros)

# 6. Entrada de lista de palavras e ordenação
palavras = input("Digite palavras separadas por espaço: ").split()
palavras.sort()
print("Palavras ordenadas:", palavras)

# 7. Entrada condicional
resposta = input("Deseja continuar? (s/n): ").lower()
if resposta == "s":
    print("Continuando...")
else:
    print("Encerrando...")
