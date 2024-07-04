import tkinter as tk;
from tkinter import messagebox

def calcular_ano_aposentadoria():
    try:
        idade_atual = int(entrada_idade_atual.get())
        idade_aposentadoria = int(entrada_idade_aposentadoria.get())
        ano_atual = 2024
        anos_restantes = idade_aposentadoria - idade_atual
        ano_aposentadoria = ano_atual + anos_restantes
        
        if anos_restantes > 0:
            mensagem = f"Você se aposentará em {ano_aposentadoria}."
        elif anos_restantes == 0:
            mensagem = "Você se aposentará este ano."
        else:
            mensagem = "Você já deveria estar aposentado!"
        
        messagebox.showinfo("Resultado", mensagem)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")


janela = tk.Tk()
janela.title("Calculadora de Aposentadoria")


label_idade_atual = tk.Label(janela, text="Digite sua idade atual:")
label_idade_atual.pack()

entrada_idade_atual = tk.Entry(janela)
entrada_idade_atual.pack()


label_idade_aposentadoria = tk.Label(janela, text="Digite a idade de aposentadoria desejada:")
label_idade_aposentadoria.pack()

entrada_idade_aposentadoria = tk.Entry(janela)
entrada_idade_aposentadoria.pack()


botao_calcular = tk.Button(janela, text="Calcular", command=calcular_ano_aposentadoria)
botao_calcular.pack()


janela.mainloop()
