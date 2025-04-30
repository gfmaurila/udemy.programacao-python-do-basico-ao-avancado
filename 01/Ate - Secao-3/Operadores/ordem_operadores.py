
# Script de exemplo: Ordem de Precedência dos Operadores em Python

# 1. Parênteses
print("1. Parênteses:", 2 * (3 + 4))  # 14

# 2. Expoente
print("2. Expoente:", 2 ** 3 ** 2)  # 2 ** (3 ** 2) = 512

# 3. Sinais unários
print("3. Sinais unários:", -3 + 2)  # -1

# 4. Multiplicação, divisão, resto, divisão inteira
print("4. Multiplicação e divisão:", 10 / 2 * 3)  # 15.0
print("   Divisão inteira:", 10 // 3)  # 3
print("   Módulo:", 10 % 3)  # 1

# 5. Soma e subtração
print("5. Soma e subtração:", 5 + 2 - 1)  # 6

# 6. Shift
print("6. Shift:", 8 >> 1, 1 << 3)  # 4 e 8

# 7. Bitwise AND
print("7. Bitwise AND:", 5 & 3)  # 1

# 8. Bitwise XOR
print("8. Bitwise XOR:", 5 ^ 3)  # 6

# 9. Bitwise OR
print("9. Bitwise OR:", 5 | 3)  # 7

# 10. Comparações
print("10. Comparações:", 3 < 5 == True)  # False (5 == True é falso)

# 11. Not lógico
print("11. not lógico:", not True)  # False

# 12. and lógico
print("12. and lógico:", True and False)  # False

# 13. or lógico
print("13. or lógico:", True or False)  # True

# 14. Atribuição
x = 10
x += 5
print("14. Atribuição:", x)  # 15
