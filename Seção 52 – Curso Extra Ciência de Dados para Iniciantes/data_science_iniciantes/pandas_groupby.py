
import pandas as pd

df = pd.read_csv("funcionarios.csv")
agrupado = df.groupby("Departamento")["Salario"].mean()
print(agrupado)
