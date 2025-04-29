
# ----------- Exemplos de print com interpolação -----------

nome = "Ana"
idade = 28
altura = 1.65

# 1. Concatenando com +
print("Olá, meu nome é " + nome + " e tenho " + str(idade) + " anos.")

# 2. Usando vírgula (automático com espaço e sem conversão)
print("Olá,", nome, "e tenho", idade, "anos.")

# 3. Usando format() com chaves
print("Olá, meu nome é {} e tenho {} anos.".format(nome, idade))

# 4. format() com índice
print("Altura: {1} m - Nome: {0}".format(nome, altura))

# 5. f-string (Python 3.6+)
print(f"Olá, meu nome é {nome}, tenho {idade} anos e {altura}m de altura.")

# 6. Estilo antigo (%)
print("Nome: %s | Idade: %d | Altura: %.2f" % (nome, idade, altura))

# Extra: formatando com f-string (decimais e alinhamento)
print(f"Altura formatada: {altura:.2f} m")         # duas casas decimais
print(f"Nome alinhado à direita: {nome:>10}")     # 10 caracteres, à direita
print(f"Nome alinhado à esquerda: {nome:<10}")    # 10 caracteres, à esquerda
