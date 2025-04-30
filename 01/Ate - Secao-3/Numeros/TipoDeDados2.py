
'''
🧮 Tipos Numéricos em Python
int – números inteiros

float – números de ponto flutuante (decimais)

complex – números complexos

bool – valores booleanos (são subclasses de int)


✅ Exemplos com print() para cada tipo:
'''

# int (inteiro)
numero_inteiro = 42
print("int:", numero_inteiro)

# float (ponto flutuante)
numero_decimal = 3.14159
print("float:", numero_decimal)

# complex (número complexo)
numero_complexo = 2 + 3j
print("complex:", numero_complexo)

# bool (valor booleano, mas é tipo numérico também!)
booleano_true = True
booleano_false = False
print("bool (True):", booleano_true)
print("bool (False):", booleano_false)



'''
🔢 Funções numéricas úteis em Python:
'''
# abs: valor absoluto
print("abs(-10):", abs(-10))

# pow: potência
print("pow(2, 3):", pow(2, 3))  # 2**3

# round: arredondamento
print("round(3.14159, 2):", round(3.14159, 2))

# divmod: retorna quociente e resto
print("divmod(10, 3):", divmod(10, 3))  # (3, 1)

# max e min
print("max(1, 2, 3):", max(1, 2, 3))
print("min(1, 2, 3):", min(1, 2, 3))

# sum: soma elementos de um iterável
print("sum([1, 2, 3]):", sum([1, 2, 3]))

# int, float, complex: funções de conversão
print("int('10'):", int('10'))
print("float('3.14'):", float('3.14'))
print("complex(1, 2):", complex(1, 2))



'''
📦 Extras da biblioteca math (para int e float):
'''
import math

print("math.sqrt(16):", math.sqrt(16))     # raiz quadrada
print("math.ceil(3.1):", math.ceil(3.1))   # teto (próximo inteiro acima)
print("math.floor(3.9):", math.floor(3.9)) # piso (próximo inteiro abaixo)
print("math.factorial(5):", math.factorial(5)) # fatorial
print("math.isclose(0.1 + 0.2, 0.3):", math.isclose(0.1 + 0.2, 0.3)) # teste de igualdade com precisão




'''
Perfeito! Vamos complementar com:

📊 Módulo statistics (média, mediana, variância…)

🧮 Módulo fractions (frações precisas)

💰 Módulo decimal (decimais com precisão arbitrária)

'''

# 📊 statistics — Estatísticas simples
import statistics

dados = [1, 2, 3, 4, 5, 5, 5, 6]

print("mean:", statistics.mean(dados))        # média
print("median:", statistics.median(dados))    # mediana
print("mode:", statistics.mode(dados))        # moda
print("variance:", statistics.variance(dados))# variância
print("stdev:", statistics.stdev(dados))      # desvio padrão

#🧮 fractions.Fraction — Números racionais exatos
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(1, 6)

print("Fraction(1, 3):", f1)
print("Fraction(1, 6):", f2)
print("Soma de frações:", f1 + f2)  # resultado exato: 1/2



#💰 decimal.Decimal — Controle de precisão decimal

from decimal import Decimal, getcontext

getcontext().prec = 5  # define a precisão global

d1 = Decimal('1.23456')
d2 = Decimal('2.34567')

print("Decimal 1:", d1)
print("Decimal 2:", d2)
print("Soma com alta precisão:", d1 + d2)











