
# 5. Avançado: List comprehensions, Decorators
quadrados = [x**2 for x in range(5)]
print("Quadrados:", quadrados)

def decorador(func):
    def interno():
        print("Antes da função")
        func()
        print("Depois da função")
    return interno

@decorador
def dizer_oi():
    print("Oi")

dizer_oi()
