
# Exemplo de app Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
