
# 2. POO: Classes, Herança, Métodos
class Animal:
    def falar(self):
        return "Som"

class Cachorro(Animal):
    def falar(self):
        return "Latido"

c = Cachorro()
print(c.falar())
