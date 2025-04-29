
import random
import statistics
from decimal import Decimal, getcontext

'''
Aqui está o script com exemplos dos módulos:

random (aleatoriedade)

statistics (estatísticas descritivas)

decimal (números com alta precisão)
'''


# ----------- Módulo random -----------
print("\n--- random ---")
print("random.random():", random.random())  # float entre 0.0 e 1.0
print("random.randint(1, 10):", random.randint(1, 10))  # int entre 1 e 10
print("random.choice([1, 2, 3]):", random.choice([1, 2, 3]))  # escolha aleatória
print("random.sample(range(10), 3):", random.sample(range(10), 3))  # amostra de 3 elementos

# ----------- Módulo statistics -----------
print("\n--- statistics ---")
dados = [1, 2, 2, 3, 4, 4, 4, 5]
print("Média:", statistics.mean(dados))
print("Mediana:", statistics.median(dados))
print("Moda:", statistics.mode(dados))
print("Desvio padrão:", statistics.stdev(dados))
print("Variância:", statistics.variance(dados))

# ----------- Módulo decimal -----------
print("\n--- decimal ---")
getcontext().prec = 6  # Define a precisão decimal global
d1 = Decimal('1.123456')
d2 = Decimal('2.345678')
print("Decimal 1:", d1)
print("Decimal 2:", d2)
print("Soma com precisão:", d1 + d2)
