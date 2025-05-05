
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 15, 13, 20]

plt.plot(x, y)
plt.title("Exemplo de Gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.savefig("grafico.png")
plt.show()
