
# Calculando idade de um funcionário
from datetime import date

class Funcionario:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.nascimento

f = Funcionario("Joana", 1990)
print(f"{f.nome} tem {f.calcular_idade()} anos.")
