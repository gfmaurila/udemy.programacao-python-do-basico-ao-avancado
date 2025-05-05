
import pandas as pd

df = pd.read_csv("funcionarios.csv")
df.to_csv("funcionarios_exportado.csv", index=False)
print("Arquivo exportado.")
