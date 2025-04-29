
# Exercício: Saudação Personalizada
# Cumprimente o usuário com base na hora do dia

nome = input("Digite seu nome: ")
hora = int(input("Digite a hora atual (0-23): "))

if 5 <= hora < 12:
    print(f"Bom dia, {nome}!")
elif 12 <= hora < 18:
    print(f"Boa tarde, {nome}!")
else:
    print(f"Boa noite, {nome}!")
