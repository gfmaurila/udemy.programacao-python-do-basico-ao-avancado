
# Solução: função para cálculo de IMC
def classificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

print(classificar_imc(70, 1.75))
