
# **kwargs com parâmetros nomeados
def apresentar_dados(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

apresentar_dados(nome="Joana", idade=28, cidade="São Paulo")
