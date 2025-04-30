
# Simulador de Financiamento Imobiliário - Completo no Terminal

def calcular_financiamento_com_extrato(valor_total, entrada, prazo_meses, juros_anual):
    valor_financiado = valor_total - entrada
    juros_mensal = (juros_anual / 100) / 12
    pmt = valor_financiado * juros_mensal / (1 - (1 + juros_mensal) ** -prazo_meses)

    extrato = []
    saldo = valor_financiado

    for mes in range(1, prazo_meses + 1):
        juros_mes = saldo * juros_mensal
        amortizacao = pmt - juros_mes
        saldo -= amortizacao
        extrato.append({
            "mes": mes,
            "prestacao": round(pmt, 2),
            "juros": round(juros_mes, 2),
            "amortizacao": round(amortizacao, 2),
            "saldo_devedor": round(max(saldo, 0), 2)
        })

    total_pago = pmt * prazo_meses
    total_juros = total_pago - valor_financiado

    return pmt, total_pago, total_juros, extrato


try:
    valor_total = float(input("Digite o valor total do imóvel: R$ "))
    entrada = float(input("Digite o valor da entrada: R$ "))
    prazo = int(input("Digite o número de meses para o financiamento: "))
    juros = float(input("Digite a taxa de juros anual (%): "))

    prestacao, total_pago, total_juros, extrato = calcular_financiamento_com_extrato(
        valor_total, entrada, prazo, juros)

    print(f"\n--- RESUMO DO FINANCIAMENTO ---")
    print(f"Prestação mensal: R$ {prestacao:.2f}")
    print(f"Total a pagar: R$ {total_pago:.2f}")
    print(f"Total em juros: R$ {total_juros:.2f}")

    ver_detalhes = input("Deseja ver os 12 primeiros meses detalhados? (s/n): ").lower()
    if ver_detalhes == "s":
        print("\nMês | Prestação | Juros | Amortização | Saldo Devedor")
        for linha in extrato[:12]:
            print(f"{linha['mes']:3} | R$ {linha['prestacao']:9.2f} | R$ {linha['juros']:6.2f} | R$ {linha['amortizacao']:11.2f} | R$ {linha['saldo_devedor']:13.2f}")

except ValueError:
    print("Erro: entradas inválidas. Use apenas números válidos.")
