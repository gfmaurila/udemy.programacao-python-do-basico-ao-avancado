
# Construtores com __init__
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p = Produto("Celular", 1200)
print(p.nome, p.preco)
