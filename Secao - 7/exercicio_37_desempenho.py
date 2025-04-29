
# Exercício: Avaliação de Desempenho
# Classifique o desempenho de um aluno

nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 9:
    print("Desempenho: Excelente")
elif nota >= 7:
    print("Desempenho: Bom")
elif nota >= 5:
    print("Desempenho: Regular")
else:
    print("Desempenho: Insuficiente")
