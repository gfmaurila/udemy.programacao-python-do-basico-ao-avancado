
# 1. Condição simples com if
idade = 20
if idade >= 18:
    print("Você é maior de idade.")

# 2. if com else
nota = 6
if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")

# 3. if, elif e else
media = 8
if media >= 9:
    print("Excelente!")
elif media >= 7:
    print("Bom!")
else:
    print("Precisa melhorar.")

# 4. if com múltiplas condições (and, or)
idade = 22
tem_carteira = True
if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

# 5. if com input
nome = input("Digite seu nome: ")
if nome.lower() == "ana":
    print("Olá, Ana!")
else:
    print(f"Olá, {nome}!")
