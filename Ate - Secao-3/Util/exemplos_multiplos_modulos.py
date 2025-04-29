
import re
import json
from pathlib import Path
import asyncio
import matplotlib.pyplot as plt
# import requests  # Comentado pois requer rede
from sklearn.linear_model import LinearRegression
import numpy as np

'''
Aqui está um super script com exemplos de:

🔍 re — expressões regulares

📦 json — serialização de dados

📂 pathlib — manipulação de arquivos e diretórios

⚙️ asyncio — programação assíncrona

📈 matplotlib — gráficos

🌐 requests — (comentado pois requer rede)

🤖 scikit-learn — modelo de regressão linear
'''



# ----------- re (expressões regulares) -----------
print("\n--- re ---")
texto = "O número é 1234 e o CEP é 56789-000"
numeros = re.findall(r"\d+", texto)
print("Números encontrados:", numeros)

# ----------- json -----------
print("\n--- json ---")
dicionario = {"nome": "Alice", "idade": 25}
json_str = json.dumps(dicionario)
print("JSON serializado:", json_str)
print("JSON desserializado:", json.loads(json_str))

# ----------- pathlib -----------
print("\n--- pathlib ---")
p = Path("")
print("Arquivos no diretório:", list(p.glob("*.py")))

# ----------- asyncio -----------
print("\n--- asyncio ---")
async def saudacao():
    await asyncio.sleep(1)
    print("Olá, mundo async!")
asyncio.run(saudacao())

# ----------- matplotlib (gráfico simples) -----------
print("\n--- matplotlib ---")
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Exemplo de gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.savefig("grafico_exemplo.png")
print("Gráfico salvo como grafico_exemplo.png")

# ----------- requests -----------
# print("\n--- requests ---")
# response = requests.get("https://httpbin.org/get")
# print("Status code:", response.status_code)
# print("JSON:", response.json())

# ----------- scikit-learn (modelo simples) -----------
print("\n--- scikit-learn ---")
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
modelo = LinearRegression()
modelo.fit(X, y)
print("Coeficiente:", modelo.coef_)
print("Intercepto:", modelo.intercept_)
print("Predição para 5:", modelo.predict([[5]])[0])
