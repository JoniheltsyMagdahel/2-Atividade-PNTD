import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

janela = tk.Tk()
janela.title("Interface Gráfica")
janela.geometry("800x400")

rotulo = tk.Label(janela, text="Bem vindo à sua primeira interfa gráfica! :)")
rotulo.pack(pady=20)
botao = tk.Button(janela, text="clique aqui ;)", command=mostrar_mensagem)
botao.pack(pady=20)

janela.mainloop()
