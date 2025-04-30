
# Exemplo básico com scikit-learn (regressão linear)
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])  # Relação linear perfeita

modelo = LinearRegression()
modelo.fit(x, y)

previsao = modelo.predict([[5]])
print("Previsão para 5:", previsao[0])
