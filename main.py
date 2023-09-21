import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

def bissecao(a, b, tol, max_iter, funcao):
    iteracao = 0
    dados = []

    while iteracao < max_iter:
        iteracao += 1
        c = (a + b) / 2.0
        fc = eval(funcao.replace('x', str(c)))
        dados.append([iteracao, a, b, c, fc, (b - a) / 2])

        if abs(fc) < tol:
            return c, dados
        elif eval(funcao.replace('x', str(a))) * fc < 0:
            b = c
        else:
            a = c

    return None, dados

def criar_interface_grafica():
    def limpar_interface():
        lbl_raiz.config(text="Raiz encontrada: ")
        entrada_funcao.delete(0, tk.END)
        entrada_intervalo.delete(0, tk.END)
        entrada_tol.delete(0, tk.END)
        entrada_max_iter.delete(0, tk.END)
        for item in treeview.get_children():
            treeview.delete(item)
        ax.clear()
        canvas.draw()

    def executar_bissecao():
        try:
            funcao = entrada_funcao.get()
            intervalo = entrada_intervalo.get()
            tol = float(entrada_tol.get())
            max_iter = int(entrada_max_iter.get())

            a, b = map(float, intervalo.split(','))

            try:
                eval(funcao.replace('x', '0')) 
            except Exception as e:
                lbl_erro.config(text="Erro: Função Inválida", foreground="red")
                return

            resultado = bissecao(a, b, tol, max_iter, funcao)

            raiz = resultado[0]
            resultado = resultado[1]

            if raiz is not None:
                lbl_raiz.config(text=f"Raiz encontrada: {raiz:.6f}", foreground="green")
            else:
                lbl_raiz.config(text="Raiz não encontrada", foreground="red")

            for item in treeview.get_children():
                treeview.delete(item)
            for linha in resultado:
                treeview.insert('', 'end', values=(int(linha[0]), linha[1], linha[2], linha[3], linha[4], linha[5]))

            iteracoes = [linha[0] for linha in resultado]
            raiz_aproximada = [linha[3] for linha in resultado]

            ax.clear()
            x = np.linspace(a, b, 400)
            y = [eval(funcao.replace('x', str(xi))) for xi in x]
            ax.plot(x, y, label='f(x)')
            ax.axhline(0, color='black', linestyle='--', linewidth=0.5)
            ax.scatter(raiz_aproximada, np.zeros_like(raiz_aproximada), color='red', label='Aproximação da Raiz', marker='o')
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            ax.legend()
            ax.set_title('Método da Bisseção para Aproximação de Raiz')
            canvas.draw()

            print("Iteração |   a    |   b    |   c    |  f(c)  |   (b-a)/2")
            print("---------------------------------------------------------")
            for linha in resultado:
                print(f"{int(linha[0]):9d} | {linha[1]:.4f} | {linha[2]:.4f} | {linha[3]:.4f} | {linha[4]:.4f} | {linha[5]:.4f}")

            
            lbl_erro.config(text="", foreground="black")

        except ValueError as e:
            lbl_erro.config(text=f"Erro: {str(e)}", foreground="red")
            lbl_raiz.config(text="", foreground="black")

    janela = tk.Tk()
    janela.title("Método da Bisseção")

    frame_funcao = ttk.Frame(janela)
    frame_funcao.pack(pady=10)

    ttk.Label(frame_funcao, text="Insira a função (use 'x' como variável):").pack(side="left")

    entrada_funcao = ttk.Entry(frame_funcao)
    entrada_funcao.pack(side="left")

    frame_intervalo = ttk.Frame(janela)
    frame_intervalo.pack(pady=10)

    ttk.Label(frame_intervalo, text="Digite o intervalo inicial [a, b] (ex: -2, 2):").pack(side="left")

    entrada_intervalo = ttk.Entry(frame_intervalo)
    entrada_intervalo.pack(side="left")

    frame_parametros = ttk.Frame(janela)
    frame_parametros.pack(pady=10)

    ttk.Label(frame_parametros, text="Digite a tolerância (ex: 1e-6):").pack(side="left")

    entrada_tol = ttk.Entry(frame_parametros)
    entrada_tol.pack(side="left")

    ttk.Label(frame_parametros, text="Digite o número máximo de iterações:").pack(side="left")

    entrada_max_iter = ttk.Entry(frame_parametros)
    entrada_max_iter.pack(side="left")

    frame_botoes = ttk.Frame(janela)
    frame_botoes.pack(pady=10)

    botao_executar = ttk.Button(frame_botoes, text="Executar Método da Bisseção", command=executar_bissecao)
    botao_executar.pack(side="left")

    botao_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_interface)
    botao_limpar.pack(side="left")

    frame_grafico_tabela = ttk.Frame(janela)
    frame_grafico_tabela.pack(pady=10)

    lbl_erro = ttk.Label(frame_grafico_tabela, text="", foreground="red")
    lbl_erro.pack()

    lbl_raiz = ttk.Label(frame_grafico_tabela, text="Raiz encontrada: ")
    lbl_raiz.pack()

    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico_tabela)
    canvas.get_tk_widget().pack()

    treeview = ttk.Treeview(frame_grafico_tabela, columns=("Iteração", "a", "b", "c", "f(c)", "(b-a)/2"))
    treeview.heading("#1", text="Iteração")
    treeview.heading("#2", text="a")
    treeview.heading("#3", text="b")
    treeview.heading("#4", text="c")
    treeview.heading("#5", text="f(c)")
    treeview.heading("#6", text="(b-a)/2")
    treeview.pack()

    janela.mainloop()

criar_interface_grafica()