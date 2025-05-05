
# Adicionando métodos à classe
class Calculadora:
    def __init__(self, valor):
        self.valor = valor

    def dobrar(self):
        return self.valor * 2

c = Calculadora(10)
print(c.dobrar())
