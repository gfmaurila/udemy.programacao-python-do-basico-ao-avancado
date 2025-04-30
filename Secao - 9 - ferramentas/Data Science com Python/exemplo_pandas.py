
# Exemplo básico com Pandas
import pandas as pd

dados = {
    "categoria": ["A", "A", "B", "B"],
    "vendas": [100, 150, 200, 130]
}

df = pd.DataFrame(dados)
print(df.head())
print("Total por categoria:")
print(df.groupby("categoria")["vendas"].sum())
