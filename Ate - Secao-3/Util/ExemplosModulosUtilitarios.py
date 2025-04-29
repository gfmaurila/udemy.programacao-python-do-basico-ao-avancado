
from fractions import Fraction
from datetime import datetime, timedelta
import itertools
import functools

'''
Aqui está o script com exemplos dos módulos:

🧮 fractions — frações exatas

📅 datetime — datas e tempos

🔁 itertools — ferramentas para laços e combinações

🛠️ functools — utilitários de funções (ex: reduce, lru_cache)
'''



# ----------- Módulo fractions -----------
print("\n--- fractions ---")
f1 = Fraction(1, 3)
f2 = Fraction(2, 6)
print("Fraction(1, 3):", f1)
print("Fraction(2, 6):", f2)
print("Soma:", f1 + f2)

# ----------- Módulo datetime -----------
print("\n--- datetime ---")
agora = datetime.now()
amanha = agora + timedelta(days=1)
print("Agora:", agora)
print("Amanhã:", amanha)
print("Diferença em horas:", (amanha - agora).total_seconds() / 3600)

# ----------- Módulo itertools -----------
print("\n--- itertools ---")
combinacoes = list(itertools.combinations([1, 2, 3], 2))
print("Combinations de [1,2,3] 2 a 2:", combinacoes)

print("Cycle de [A, B] (primeiros 4):", [next(itertools.cycle(['A', 'B'])) for _ in range(4)])

# ----------- Módulo functools -----------
print("\n--- functools ---")
soma = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("Soma com reduce:", soma)

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci(10) com cache:", fib(10))
