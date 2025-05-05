
import pandas as pd

df = pd.read_csv("funcionarios.csv")
df["Bonus"] = df["Salario"] * 0.1
print(df)
