
# 1. if com else simples
numero = 7
if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")

# 2. if, elif, else com múltiplas opções
nota = 5
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
else:
    print("Insuficiente")

# 3. else em um loop for (executa se não houver break)
for i in range(5):
    if i == 3:
        print("Interrompido no 3")
        break
else:
    print("Loop terminou sem break")

# 4. else com while
contador = 0
while contador < 3:
    print("Contando:", contador)
    contador += 1
else:
    print("Loop while finalizado normalmente")
