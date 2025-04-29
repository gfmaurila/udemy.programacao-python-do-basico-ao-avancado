
import csv
import os
import pandas as pd

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

def mostrar_dados():
    if not os.path.exists(arquivo_csv):
        print("Nenhum dado cadastrado ainda.")
        return
    df = pd.read_csv(arquivo_csv, names=["Nome", "Idade", "Cidade", "Salário"])
    print("\n--- CADASTROS ---")
    print(df)

def analisar_dados():
    if not os.path.exists(arquivo_csv):
        print("Nenhum dado para análise.")
        return
    df = pd.read_csv(arquivo_csv, names=["Nome", "Idade", "Cidade", "Salário"])
    print("\n--- ANÁLISE ---")
    print("Média salarial: R$ {:.2f}".format(df["Salário"].mean()))
    print("Pessoa mais jovem:", df.loc[df["Idade"].idxmin()]["Nome"])
    print("Pessoa mais velha:", df.loc[df["Idade"].idxmax()]["Nome"])

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar todos os cadastros")
    print("3 - Analisar dados")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        mostrar_dados()
    elif opcao == "3":
        analisar_dados()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
