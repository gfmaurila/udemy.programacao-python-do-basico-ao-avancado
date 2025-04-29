
# 1. Múltiplos inteiros separados por espaço
entrada = input("Digite 3 números inteiros separados por espaço: ")
try:
    n1, n2, n3 = map(int, entrada.split())
    print(f"Números digitados: {n1}, {n2}, {n3}")
except ValueError:
    print("Erro: digite exatamente 3 números.")

# 2. Nome e idade separados por vírgula
entrada = input("Digite seu nome e idade separados por vírgula (ex: Ana,30): ")
try:
    nome, idade = entrada.split(",")
    idade = int(idade.strip())
    print(f"Nome: {nome.strip()} | Idade: {idade}")
except ValueError:
    print("Erro: entrada inválida. Use o formato: Nome,Idade")

# 3. Lista de palavras separadas por espaço
palavras = input("Digite palavras separadas por espaço: ").split()
print("Palavras digitadas:", palavras)

# 4. Lista de números decimais separados por vírgula
entrada = input("Digite valores decimais separados por vírgula: ")
try:
    numeros = list(map(lambda x: float(x.replace(",", ".").strip()), entrada.split(",")))
    print("Números convertidos:", numeros)
except ValueError:
    print("Erro: certifique-se de digitar apenas números válidos separados por vírgula.")
