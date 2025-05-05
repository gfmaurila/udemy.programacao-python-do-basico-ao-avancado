
# Desafio: calcular litros de tinta para pintura
# 1 litro cobre 3m². Lata tem 18L.

area = float(input("Digite a área a ser pintada em m²: "))
litros = area / 3
latas = -(-litros // 18)  # arredondamento para cima

print(f"Você precisará de {int(latas)} latas de tinta.")
