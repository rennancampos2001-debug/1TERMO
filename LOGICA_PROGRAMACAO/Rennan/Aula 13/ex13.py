# Exercicio - crie uma aplicação que faça o calculo de idade de pessoas
# Deve perguntar o nome da pessoa e o ano de nascimento
import tkinter as tk
from tkinter import messagebox

def registre_usuario():
    nome_usuario = ent_nome_usuario
    idade_usuario = int(ent_idade_usuario.get())

    idade=  2026 - idade_usuario

    if idade_usuario == "" and nome_usuario == "":
        messagebox.showwarning("Sem informação", "Por favor, coloque seu ano de nascimento e nome!")
    else:
        messagebox.showinfo("Concluido!",f"Olá {nome_usuario}\n A sua idade é de: {idade} ! ")

janela = tk.Tk()
janela.title("Calculo de idade")
janela.geometry("900x400")
janela.configure(bg="Blue")



lbl_nome_usuario= tk.Label(janela,text="Qual é o seu nome ?",font=("Monocraft", 14),fg="Black")
lbl_nome_usuario.grid(row=1,column=0, padx=10,pady=10)
lbl_idade_usuario= tk.Label(janela,text="Quando você nasceu ?",font=("Monocraft", 14),fg="Black")
lbl_idade_usuario.grid(row=2,column=0,padx=10,pady=10)


ent_nome_usuario= tk.Entry(janela,font=("Monocraft", 14), width=30,fg="#000000")
ent_nome_usuario.grid(row=1,column=1,padx=10,pady=10)
ent_idade_usuario= tk.Entry(janela,font=("Monocraft", 14),width=30, fg="#000000")
ent_idade_usuario.grid(row=2,column=1,padx=10,pady=10)

btn_realizar_cadastro= tk.Button(janela,text="Calcular",font=("Monocraft", 14), fg="#00FF7F",command=registre_usuario)
btn_realizar_cadastro.grid(row= 5, column=1, padx=10, pady=10)
btn_sair_janela= tk.Button(janela,text="Sair",font=("Monocraft", 14),fg="#FF0000",command=janela.destroy)
btn_sair_janela.grid(row=6,column=1,padx=10,pady=10)

janela.mainloop()