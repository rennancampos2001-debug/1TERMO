import tkinter as tk
from tkinter import messagebox

lista_funcionarios = []
usuarios_cadastrado = 0
total_em_dia = 0

janela = tk.Tk()
janela.title("Cadastro na Brigada de incendio")
janela.geometry("1920x1080")

def cadastro():
    global usuarios_cadastrado, total_em_dia

    nome_txt = nome.get()
    setor_txt = setor.get()
    nr10_txt = nr10.get()
    nr35_txt = nr35.get()
    brigada_txt = brigada.get()

    try:
        treino = int(treino.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas numero de ano")
        return
    
    funcionario = {
        "nome": nome_txt,
        "setor": setor_txt,
        "nr10": nr10_txt,
        "nr35": nr35_txt,
        "brigada": brigada_txt, 
        "treino": treino_txt
    }

    lista_funcionarios.append(funcionario)

    usuarios_cadastrado = len(lista_funcionarios)

    nome.delete(0,tk.END)
    setor.delete(0,tk.END)
    nr10.delete(0,tk.END)
    nr35.delete(0,tk.END)
    brigada.delete(0,tk.END)
    treino.delete(0,tk.END)

    messagebox.showinfo("Sucesso", f"Funcionario {nome_txt} cadastrado com sucesso! ")

def relatorio():
    messagebox.showinfo("Cadastros totais", f"Usuarios cadastrados: {len (usuarios_cadastrado)}")


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


btn_cadastre = tk.Button(janela,text=("Cadastrar"),font=("Monocraft", 12), command=cadastro)


btn_relatorio = tk.Button(janela,text=("Ver relatorio final"),font=("Monocraft", 12), command=relatorio)


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
btn_relatorio.pack(pady=5)

janela.mainloop()