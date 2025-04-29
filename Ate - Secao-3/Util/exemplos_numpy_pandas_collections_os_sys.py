
import numpy as np
import pandas as pd
from collections import Counter, defaultdict, namedtuple
import os
import sys

'''
Aqui está o arquivo com exemplos de:

📊 numpy — arrays e operações matemáticas

🐼 pandas — análise de dados com tabelas (DataFrame)

🧰 collections — estruturas de dados úteis (Counter, defaultdict, namedtuple)

📁 os — interações com o sistema de arquivos

🖥️ sys — informações do sistema e ambiente Python
'''


# ----------- numpy -----------
print("\n--- numpy ---")
arr = np.array([1, 2, 3, 4])
print("Array:", arr)
print("Média:", np.mean(arr))
print("Soma:", np.sum(arr))
print("Matriz identidade (3x3):\n", np.eye(3))

# ----------- pandas -----------
print("\n--- pandas ---")
df = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 35, 31]
})
print("DataFrame:\n", df)
print("Média de idade:", df["Idade"].mean())

# ----------- collections -----------
print("\n--- collections ---")
contagem = Counter("banana")
print("Counter de 'banana':", contagem)

d = defaultdict(int)
d["chave_inexistente"] += 1
print("defaultdict com int:", d)

Pessoa = namedtuple("Pessoa", ["nome", "idade"])
p = Pessoa("João", 30)
print("NamedTuple Pessoa:", p.nome, p.idade)

# ----------- os -----------
print("\n--- os ---")
print("Diretório atual:", os.getcwd())
print("Listando arquivos:", os.listdir(""))

# ----------- sys -----------
print("\n--- sys ---")
print("Versão do Python:", sys.version)
print("Caminho dos módulos:", sys.path)
