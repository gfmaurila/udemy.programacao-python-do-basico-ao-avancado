
📦 GUIA DE FERRAMENTAS E BIBLIOTECAS PYTHON COM EXEMPLOS

---

🔹 FLASK - Criação de Aplicações Web

📘 O que é:
Framework leve para criar APIs e sites com Python.

📄 Exemplo:
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Flask!"

app.run(debug=True)

---

🔹 DJANGO - Framework Web Completo

📘 O que é:
Framework robusto e completo para aplicações web com autenticação, ORM e painel administrativo.

📄 Exemplo de View:
from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Olá, Django!")

---

🔹 SCRAPY - Coleta de Dados (Web Scraping)

📘 O que é:
Framework para extrair dados de sites (scraping) de forma rápida e estruturada.

📄 Exemplo:
import scrapy

class MeuSpider(scrapy.Spider):
    name = "exemplo"
    start_urls = ['https://example.com']

    def parse(self, response):
        titulo = response.xpath('//title/text()').get()
        print("Título:", titulo)

---

🔹 KERAS - Machine Learning e Deep Learning

📘 O que é:
Biblioteca de alto nível para criar redes neurais com poucas linhas de código.

📄 Exemplo:
from keras.models import Sequential
from keras.layers import Dense

modelo = Sequential()
modelo.add(Dense(units=10, input_dim=2, activation='relu'))
modelo.add(Dense(units=1, activation='sigmoid'))
modelo.compile(loss='binary_crossentropy', optimizer='adam')
print(modelo.summary())

---

🔹 PIP - Gerenciador de Pacotes

📘 O que é:
Comando usado para instalar bibliotecas do Python.

📄 Exemplo:
pip install pandas
pip install flask

---

🔹 PANDAS - Análise de Dados

📘 O que é:
Biblioteca para manipular e analisar dados estruturados (como tabelas).

📄 Exemplo:
import pandas as pd

df = pd.read_csv("dados.csv")
print(df.groupby("categoria")["valor"].sum())

---

🔹 NUMPY - Cálculo Numérico e Vetorial

📘 O que é:
Biblioteca para cálculos rápidos com arrays, vetores e matrizes.

📄 Exemplo:
import numpy as np

valores = np.array([1, 2, 3])
print("Soma:", np.sum(valores))
print("Média:", np.mean(valores))

---

🔹 SQLITE - Banco de Dados Local

📘 O que é:
Banco de dados leve embutido no Python (sem precisar instalar nada).

📄 Exemplo:
import sqlite3

con = sqlite3.connect("banco.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT)")
cursor.execute("INSERT INTO clientes (nome) VALUES ('Maria')")
con.commit()

for linha in cursor.execute("SELECT * FROM clientes"):
    print(linha)

con.close()

---

Essas bibliotecas são essenciais para automação, ciência de dados, web, inteligência artificial e banco de dados.
