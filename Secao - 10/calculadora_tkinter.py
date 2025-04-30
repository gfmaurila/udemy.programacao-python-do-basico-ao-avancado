
import tkinter as tk
from tkinter import messagebox

historico = []

def calcular(op):
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())

        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "*":
            resultado = a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero")
            resultado = a / b
        elif op == "**":
            resultado = a ** b
        else:
            raise ValueError("Operação inválida")

        historico.append(f"{a} {op} {b} = {resultado}")
        saida["text"] = f"Resultado: {resultado:.2f}"

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def mostrar_historico():
    messagebox.showinfo("Histórico", "\n".join(historico) if historico else "Nenhuma operação realizada ainda.")

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Calculadora com Histórico")

tk.Label(janela, text="Número 1:").grid(row=0, column=0)
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1)

tk.Label(janela, text="Número 2:").grid(row=1, column=0)
entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=1)

botoes = ["+", "-", "*", "/", "**"]
for i, op in enumerate(botoes):
    tk.Button(janela, text=op, width=5, command=lambda o=op: calcular(o)).grid(row=2, column=i)

saida = tk.Label(janela, text="Resultado:")
saida.grid(row=3, column=0, columnspan=5)

tk.Button(janela, text="Histórico", command=mostrar_historico).grid(row=4, column=0, columnspan=5)

janela.mainloop()
