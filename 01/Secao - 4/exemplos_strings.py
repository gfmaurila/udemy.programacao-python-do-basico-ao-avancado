
'''
🧪 Transformações (upper, lower, capitalize, etc.)

🔍 Busca e substituição

✂️ Fatiamento

🔗 Split e Join

✅ Verificações (isalnum, isdigit, etc.)

🧾 Formatação moderna (f-string, .format())
'''



# ----------- Operações básicas com strings -----------
texto = "Python é incrível!"

print("Texto original:", texto)
print("Tamanho:", len(texto))
print("Minúsculas:", texto.lower())
print("Maiúsculas:", texto.upper())
print("Primeira maiúscula:", texto.capitalize())
print("Título:", texto.title())
print("Inverso:", texto[::-1])

# ----------- Busca e substituição -----------
print("Começa com 'Python'?", texto.startswith("Python"))
print("Termina com '!'?", texto.endswith("!"))
print("Posição de 'é':", texto.find("é"))
print("Substituir 'incrível' por 'poderoso':", texto.replace("incrível", "poderoso"))

# ----------- Fatiamento e índices -----------
print("Primeiros 6 caracteres:", texto[:6])
print("Últimos 3 caracteres:", texto[-3:])

# ----------- Divisão e junção -----------
palavras = texto.split()
print("Split:", palavras)
print("Join com hífen:", "-".join(palavras))

# ----------- Verificações -----------
print("É alfanumérico?", "abc123".isalnum())
print("É numérico?", "123".isdigit())
print("É letra?", "Python".isalpha())
print("Contém apenas espaços?", "   ".isspace())

# ----------- Formatação moderna -----------
nome = "Ana"
idade = 28
print(f"{nome} tem {idade} anos.")  # f-string
print("{0} tem {1} anos.".format(nome, idade))  # format
