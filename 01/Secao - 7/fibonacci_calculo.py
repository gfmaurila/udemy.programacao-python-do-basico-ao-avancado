
# Fibonacci - Versão Iterativa
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\n")

# Fibonacci - Versão Recursiva
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

termos = int(input("Digite quantos termos deseja ver (recursivo): "))
for i in range(termos):
    print(fibonacci(i), end=" ")
