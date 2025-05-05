
import pandas as pd

df = pd.read_csv("funcionarios.csv")
filtrados = df[df["Idade"] > 30]
print(filtrados)
