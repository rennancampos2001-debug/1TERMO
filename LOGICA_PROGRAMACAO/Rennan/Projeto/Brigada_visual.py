import tkinter as tk
from tkinter import messagebox

usuarios_cadastrado = 0
total_em_dia = 0

janela = tk.Tk()
janela.title("Cadastro na Brigada de incendio")
janela.geometry("1920x1080")

def cadastro():
    global usuarios_cadastrado, total_em_dia

    nome = guarda_nome.get()
    setor = qual_setor.get()
    nr10 = tem_nr10.get()
    nr35 = tem_nr35.get()
    brigada = tem_brigada.get()

    try:
        treino = int(ano_treino.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas numero de ano")

    usuarios_cadastrado += 1


def relatorio():
    messagebox.showinfo("Cadastros totais", f"Usuarios cadastrados: {usuarios_cadastrado}")


lbl_titulo = tk.Label(janela,text=("Dados do funcionario"),font=("Monocraft", 16, "bold"))


lbl_nome = tk.Label(janela, text=("Qual é o seu nome?"), font=("Monocraft", 16))
nome = tk.Entry(janela,font=("Monocraft", 14))


lbl_setores = tk.Label(janela, text=("Qual é o seu setor? (Elétrica/Altura)"), font=("Monocraft", 14))
setor = tk.Entry(janela,font=("Monocraft", 14))


lbl_nr10 = tk.Label(janela, text=("Você fez o treinamento NR10 ? (Sim/Não)"), font=("Monocraft", 14))
nr10 = tk.Entry(janela,font=("Monocraft", 14))


lbl_nr35 = tk.Label(janela, text=("Você fez o treinamento NR35? (Sim/Não)"), font=("Monocraft", 14))
nr35 = tk.Entry(janela,font=("Monocraft", 14))


lbl_brigada = tk.Label(janela, text=("Voce fez o treinamento da Brigada? (Sim/Não)"), font=("Monocraft", 14))
brigada = tk.Entry(janela,font=("Monocraft", 14))


lbl_treino = tk.Label(janela, text=("Em que ano você fez o treinamento?"), font=("Monocraft", 14))
treino = tk.Entry(janela,font=("Monocraft", 14))


btn_cadastre = tk.Button(janela,text=("Cadastrar"),font=("Monocraft", 12))


btn_relatorio = tk.Button(janela,text=("Ver relatorio final"),font=("Monocraft", 12))


lbl_titulo.pack(pady=25)
lbl_nome.pack(pady=10)
nome.pack(pady=1)
lbl_setores.pack(pady=10)
setor.pack(pady=1)
lbl_nr10.pack(pady=10)
nr10.pack(pady=1)
lbl_nr35.pack(pady=10)
nr35.pack(pady=1)
lbl_brigada.pack(pady=10)
brigada.pack(pady=1)
lbl_treino.pack(pady=10)
treino.pack(pady=1)
btn_cadastre.pack(pady=10)
btn_cadastre.pack(pady=5)

janela.mainloop()