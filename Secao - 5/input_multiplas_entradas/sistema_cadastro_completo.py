
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

arquivo_csv = "cadastros.csv"

def cadastrar():
    entrada = input("Digite nome, idade, cidade e salário separados por vírgula: ")
    try:
        nome, idade, cidade, salario = entrada.split(",")
        idade = int(idade.strip())
        salario = float(salario.strip().replace(",", "."))
        with open(arquivo_csv, mode="a", newline='', encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow([nome.strip(), idade, cidade.strip(), salario])
        print("Cadastro salvo com sucesso!")
    except ValueError:
        print("Erro: dados inválidos. Use o formato: nome,idade,cidade,salário")

def carregar_dados():
    if not os.path.exists(arquivo_csv):
        print("Nenhum dado cadastrado ainda.")
        return None
    df = pd.read_csv(arquivo_csv, names=["Nome", "Idade", "Cidade", "Salário"])
    return df

def mostrar_dados():
    df = carregar_dados()
    if df is not None:
        print("\n--- CADASTROS ---")
        print(df)

def analisar_dados():
    df = carregar_dados()
    if df is None:
        return
    print("\n--- ANÁLISE ---")
    print("Média salarial: R$ {:.2f}".format(df["Salário"].mean()))
    print("Pessoa mais jovem:", df.loc[df["Idade"].idxmin()]["Nome"])
    print("Pessoa mais velha:", df.loc[df["Idade"].idxmax()]["Nome"])

def filtrar_por_cidade():
    df = carregar_dados()
    if df is None:
        return
    cidade = input("Digite o nome da cidade para filtrar: ").strip().lower()
    filtrado = df[df["Cidade"].str.lower() == cidade]
    print(f"\n--- Pessoas de {cidade.title()} ---")
    print(filtrado)

def filtrar_por_faixa_etaria():
    df = carregar_dados()
    if df is None:
        return
    try:
        idade_min = int(input("Idade mínima: "))
        idade_max = int(input("Idade máxima: "))
        filtrado = df[(df["Idade"] >= idade_min) & (df["Idade"] <= idade_max)]
        print(f"\n--- Pessoas entre {idade_min} e {idade_max} anos ---")
        print(filtrado)
    except ValueError:
        print("Erro: Idades inválidas.")

def gerar_graficos():
    df = carregar_dados()
    if df is None:
        return
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    df["Idade"].plot(kind="hist", bins=10, title="Distribuição de Idade")
    plt.subplot(1, 2, 2)
    df["Salário"].plot(kind="hist", bins=10, title="Distribuição de Salário")
    plt.tight_layout()
    plt.savefig("graficos_cadastro.png")
    print("Gráficos salvos como 'graficos_cadastro.png'")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar todos os cadastros")
    print("3 - Analisar dados")
    print("4 - Filtrar por cidade")
    print("5 - Filtrar por faixa etária")
    print("6 - Gerar gráficos")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        mostrar_dados()
    elif opcao == "3":
        analisar_dados()
    elif opcao == "4":
        filtrar_por_cidade()
    elif opcao == "5":
        filtrar_por_faixa_etaria()
    elif opcao == "6":
        gerar_graficos()
    elif opcao == "7":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
