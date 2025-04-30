
'''
Aqui está o script com exemplos de listas (arrays) de strings em Python:

📥 Acesso e fatiamento

➕ Adição e inserção

❌ Remoção (remove, pop)

🔃 Ordenação e reversão

🔍 Verificações e filtros

🔁 Compreensões de lista para transformar ou filtrar
'''

# ----------- Lista de strings -----------
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

print("Lista original:", nomes)

# Acessos e fatiamento
print("Primeiro nome:", nomes[0])
print("Últimos dois nomes:", nomes[-2:])

# Adicionar elementos
nomes.append("Fernanda")
print("Após append:", nomes)

# Inserir em posição específica
nomes.insert(2, "Gabriel")
print("Após insert:", nomes)

# Remover por valor
nomes.remove("Carlos")
print("Após remover 'Carlos':", nomes)

# Remover último
ultimo = nomes.pop()
print("Após pop():", nomes)
print("Elemento removido:", ultimo)

# Ordenação
nomes.sort()
print("Ordenado:", nomes)

# Ordenação reversa
nomes.sort(reverse=True)
print("Ordem reversa:", nomes)

# Tamanho
print("Quantidade de nomes:", len(nomes))

# Verificar existência
print("'Ana' está na lista?", "Ana" in nomes)

# Iterar e transformar
maiusculos = [nome.upper() for nome in nomes]
print("Todos maiúsculos:", maiusculos)

# Filtrar nomes com mais de 5 letras
longos = [nome for nome in nomes if len(nome) > 5]
print("Nomes com mais de 5 letras:", longos)
