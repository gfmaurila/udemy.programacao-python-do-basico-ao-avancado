
# 💼 Exemplos de Carreiras com Python

# 1️⃣ AUTOMATION
# Exemplo: Renomear arquivos em massa
import os

print("🔁 Renomeando arquivos em 'pasta/'")
# for i, filename in enumerate(os.listdir("pasta/")):
#     os.rename(f"pasta/{filename}", f"pasta/arquivo_{i}.txt")


# 2️⃣ WEB DEVELOPER
# Exemplo: Criar uma rota com Flask
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Bem-vindo ao meu site em Flask!"

# app.run(debug=True)


# 3️⃣ ETHICAL HACKER
# Exemplo: Scanner de portas
import socket

ip = "127.0.0.1"
print(f"🔎 Escaneando portas em {ip}")
for port in range(70, 75):
    s = socket.socket()
    if s.connect_ex((ip, port)) == 0:
        print(f"Porta {port} ABERTA")
    s.close()


# 4️⃣ GAME DEVELOPER
# Exemplo: Janela simples com pygame
# import pygame
# pygame.init()

# tela = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Meu Jogo")

# while True:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             exit()


# 5️⃣ DATA SCIENTIST
# Exemplo: Análise de dados com pandas
import pandas as pd

dados = {
    "produto": ["caneta", "caneta", "lápis", "lápis"],
    "valor": [2.50, 3.00, 1.50, 1.80]
}
df = pd.DataFrame(dados)

print("\n📊 Total por produto:")
print(df.groupby("produto")["valor"].sum())
