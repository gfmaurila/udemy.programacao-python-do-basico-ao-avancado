
# 1. Avaliação de nota
nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
elif nota >= 5:
    print("Regular.")
else:
    print("Reprovado.")

# 2. Classificação por idade
idade = 16

if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

# 3. Menu com múltiplas opções
opcao = input("Escolha uma opção (1, 2 ou 3): ")

if opcao == "1":
    print("Você escolheu Opção 1")
elif opcao == "2":
    print("Você escolheu Opção 2")
elif opcao == "3":
    print("Você escolheu Opção 3")
else:
    print("Opção inválida")
