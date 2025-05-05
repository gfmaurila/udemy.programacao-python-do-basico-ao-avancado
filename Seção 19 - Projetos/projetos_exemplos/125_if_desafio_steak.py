
# Desafio: ponto do steak
ponto = input("Como você quer seu steak? (mal passado / ao ponto / bem passado): ").lower()
if ponto == "mal passado":
    print("Seu steak ficará vermelho por dentro.")
elif ponto == "ao ponto":
    print("Seu steak ficará rosado por dentro.")
elif ponto == "bem passado":
    print("Seu steak ficará marrom por dentro.")
else:
    print("Opção inválida.")
