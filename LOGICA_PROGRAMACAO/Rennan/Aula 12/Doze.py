#TKINTER

# Componentes Widgets
# ttk: Tk( # Janela
# lb: Label() # Rotulo
# br: Button() # Botão
# et: Entry() # Caixa de texto

import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira janela GUI")
janela.configure(bg="#f0f0f0")
janela.geometry("800x500") #Largura x Altura

# 2. Criar a função do botão (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão")

# 3. Criar os componentes
lbl_titulo = tk.Label(
    janela, 
    text="Bem vindo a nossa aula de tkinter",
    font=("Arial", 14, "bold")
 )

btn_clique = tk.Button(
    janela,
    text="Clique aqui", 
    font=("Arial",11),
     bg="#2ecc71", 
     fg="white", 
     command=mostrar_mensagem
)

btn_close = tk.Button(
    janela, 
    text="Fechar", 
    font=("Arial", 11, "bold"), 
    bg="#cc2e2e", 
    command=janela.destroy
)

# 4.Posicionar os componentes
lbl_titulo.pack(pady=50) # 'pady' adiciona um espaçamento vertrical
btn_clique.pack(pady=20)
btn_close.pack(pady=20)

# 5. Rodar o loop da interface
janela.mainloop()