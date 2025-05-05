
# Try e Except com listas
lista = [1, 2, 3]

try:
    print(lista[5])
except IndexError:
    print("Erro: índice fora da lista")
