
# Solução: usando sets para interseção
def funcionarios_em_comum(a, b):
    return a & b

print(funcionarios_em_comum({"Ana", "Carlos"}, {"Carlos", "João"}))
