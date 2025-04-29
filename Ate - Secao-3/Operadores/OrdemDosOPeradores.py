

'''

Boa! A ordem dos operadores em Python (também chamada de precedência de operadores) define quem é avaliado primeiro numa expressão matemática ou lógica.

Aqui está a ordem do mais alto para o mais baixo, com exemplos práticos.


🧠 Ordem de Precedência dos Operadores Python


Precedência | Tipo | Operador(es) | Exemplo
1 | Parênteses | ( ) | 2 * (3 + 4) → 14
2 | Expoente | ** | 2 ** 3 → 8
3 | Sinais unários | +x, -x, ~x | -5
4 | Multiplicação e divisão | *, /, //, % | 10 / 2 * 3 → 15.0
5 | Adição e subtração | +, - | 5 + 2 - 1 → 6
6 | Shift | <<, >> | 8 >> 1 → 4
7 | Bitwise AND | & | 5 & 3 → 1
8 | Bitwise XOR | ^ | 5 ^ 3 → 6
9 | Bitwise OR | ` | `
10 | Comparações | ==, !=, >, <, >=, <=, is, is not, in, not in | 3 < 5 == True → True
11 | Not lógico | not | not True → False
12 | And lógico | and | True and False → False
13 | Or lógico | or | True or False → True
14 | Atribuição | =, +=, -=, etc | x = 5

'''


#🧪 Exemplos:

print(2 + 3 * 4)        # 14 (multiplicação antes da soma)
print((2 + 3) * 4)      # 20 (parênteses antes)
print(2 ** 3 ** 2)      # 512 (potência é associativa à direita: 2 ** (3 ** 2))
print(not True or False) # False (not vem antes de or)
print(10 > 5 and 2 < 3) # True




# ✅ Resultado dos exemplos:
'''
1. Parênteses: 14
2. Expoente: 512
3. Sinais unários: -1
4. Multiplicação e divisão: 15.0
   Divisão inteira: 3
   Módulo: 1
5. Soma e subtração: 6
6. Shift: 4 8
7. Bitwise AND: 1
8. Bitwise XOR: 6
9. Bitwise OR: 7
10. Comparações: False   ← (explicação abaixo)
11. not lógico: False
12. and lógico: False
13. or lógico: True
14. Atribuição: 15

'''

# 🔍 Nota sobre a linha 10:
print("10. Comparações:", 3 < 5 == True)  # False

#Isso é avaliado como:
# (3 < 5) and (5 == True) → True and False → False


# Se quiser testar exclusivamente se 3 < 5 for igual a True, use:
print(3 < 5 == True)      # False (como acima)
print((3 < 5) == True)    # True (se for essa sua intenção)











