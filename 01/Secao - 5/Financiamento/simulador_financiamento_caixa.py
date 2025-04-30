
# Simulador de Financiamento Imobiliário - Caixa Econômica Federal

def calcular_financiamento(valor_total, entrada, prazo_meses, juros_anual):
    valor_financiado = valor_total - entrada
    juros_mensal = (juros_anual / 100) / 12

    # Fórmula da Tabela PRICE
    pmt = valor_financiado * juros_mensal / (1 - (1 + juros_mensal) ** -prazo_meses)
    total_pago = pmt * prazo_meses
    total_juros = total_pago - valor_financiado

    return pmt, total_pago, total_juros

try:
    valor_total = float(input("Digite o valor total do imóvel: R$ "))
    entrada = float(input("Digite o valor de entrada: R$ "))
    prazo_meses = int(input("Digite a quantidade de meses (prazo): "))
    juros_anual = float(input("Digite a taxa de juros anual (%): "))

    prestacao, total, juros = calcular_financiamento(valor_total, entrada, prazo_meses, juros_anual)

    print(f"\nValor da prestação mensal: R$ {prestacao:.2f}")
    print(f"Valor total a ser pago: R$ {total:.2f}")
    print(f"Valor total em juros: R$ {juros:.2f}")
except ValueError:
    print("Erro: entradas inválidas. Verifique os valores digitados.")
