
# 6. Frameworks Web: Exemplo com Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo ao Flask!"

# app.run(debug=True)  # Descomente para rodar localmente
