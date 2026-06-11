# Revisão Tkinter



import tkinter as tk
from tkinter import messagebox,ttk



# DEF funções em bloco
def cadastrar_usuario():
    # .get
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_qual_curso.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" and curso_usuario == "" and nome_escola =="":
        messagebox.showwarning("Bem vindo", "Digite seu nome, seu curso e sua escola")
    else:
        messagebox.showinfo("Bem vindo",f"Olá {nome_usuario}!\n Curso: {curso_usuario}\n Escola: {nome_escola}")



# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("750x750")
janela.configure(bg="#00BFFF")



# 1 - Etapa Componentes
# Labels = Rótulos ou nossos antigos prints
lbl_nome_usuario = tk.Label(janela,text="Qual é o seu nome ?",font=("Monocraft", 14),fg="Green")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)
lbl_qual_curso = tk.Label(janela,text="Qual é o seu curso ?",font=("Monocraft", 14),fg="Green")
lbl_qual_curso.grid(row=1, column=0, pady=10, padx=10)
lbl_nome_escola = tk.Label(janela, text="Escolha sua Escola.:", font=("Monocraft", 14), fg="Green")
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)



# Entrys = caixa de texto antigos input
ent_nome_usuario = tk.Entry(janela, font= ("Monocraft", 12), width=30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)
ent_qual_curso = tk.Entry(janela,font=("Monocreft",12), width=30)
ent_qual_curso.grid(row=1, column=1, pady=10, padx= 10)



# ComBox = Caixa de seleção
cmb_nome_escola = ttk.Combobox(janela, values=["SESI005","SESI408"],font=("Monocraft", 14), state="readonly")
cmb_nome_escola.grid(row=2, column=1,pady=10,padx=10)



# Botões = Botões de clique
btn_realizar_cadastro = tk.Button(janela,text="Cadastrar",font=("Monocraft", 14), fg="Green", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=5, column=1,pady=10,padx=10)
btn_fechar_janela = tk.Button(janela,text="Fechar",font=("Monocraft",14),fg="Red",command=janela.destroy)
btn_fechar_janela.grid(row=6, column=1,pady=10,padx=10)



# 4 - Etapa Loop
janela.mainloop()