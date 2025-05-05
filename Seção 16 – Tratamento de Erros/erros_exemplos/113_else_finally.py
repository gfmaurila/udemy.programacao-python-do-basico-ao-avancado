
# Else e Finally com try
try:
    print("Executando try")
    resultado = 10 / 2
except ZeroDivisionError:
    print("Erro de divisão")
else:
    print("Sem erros, resultado:", resultado)
finally:
    print("Isso sempre será executado (try concluído)")
