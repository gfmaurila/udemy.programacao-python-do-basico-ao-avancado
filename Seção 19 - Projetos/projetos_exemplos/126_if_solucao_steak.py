
# Solução do desafio: ponto do steak
def ponto_steak(ponto):
    mapa = {
        "mal passado": "vermelho por dentro",
        "ao ponto": "rosado por dentro",
        "bem passado": "marrom por dentro"
    }
    return mapa.get(ponto.lower(), "Opção inválida.")

print(ponto_steak("mal passado"))
