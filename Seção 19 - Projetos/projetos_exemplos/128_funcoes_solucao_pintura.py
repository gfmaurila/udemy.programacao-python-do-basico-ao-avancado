
# Solução: função de pintura
import math

def calcular_pintura(area):
    litros = area / 3
    latas = math.ceil(litros / 18)
    return latas

print("Latas necessárias:", calcular_pintura(100))
