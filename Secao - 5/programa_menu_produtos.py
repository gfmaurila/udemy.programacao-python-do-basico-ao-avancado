
# Programa com menu para calcular 10% de acréscimo em múltiplos produtos

def calcular_preco_com_acrescimo(valor):
    acrescimo = valor * 0.10
    valor_final = valor + acrescimo
    return valor, acrescimo, valor_final

while True:
    print("\n--- MENU ---")
    print("1 - Calcular preço com acréscimo de 10%")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor = float(input("Digite o valor do produto: R$ "))
            original, acrescimo, total = calcular_preco_com_acrescimo(valor)
            print(f"Valor original: R$ {original:.2f}")
            print(f"Acréscimo de 10%: R$ {acrescimo:.2f}")
            print(f"Valor final com acréscimo: R$ {total:.2f}")
        except ValueError:
            print("Erro: entrada inválida. Digite um número válido.")
    elif opcao == "2":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

