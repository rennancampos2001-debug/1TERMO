import tkinter as tk
from tkinter import messagebox

usuarios_cadastrado = 0
total_em_dia = 0

janela = tk.Tk()
janela.title("Cadastro na Brigada de incendio")
janela.geometry("1920x1080")

def alerta_reciclagem(ano_treino):
    ano_atual = 2026 
    if (ano_atual - ano_treino) > 2:
        return "Treinamento Vencido! Encaminhar para reciclagem.", False
    else:
        return "Treinamento Válido.", True

def cadastro():
    global usuarios_cadastrado, total_em_dia


    str_nome = nome.get()
    str_setor = setor.get()
    str_nr10 = nr10.get()
    str_nr35 = nr35.get()
    str_brigada = brigada.get()

    try:
    
        ano_treino_int = int(treino.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas número de ano (Ex: 2024)")
        return 

    usuarios_cadastrado += 1

    mensagem_epi = "Nenhum EPI obrigatório específico listado para este setor."
    if str_setor.strip().lower() == "elétrica" or str_setor.strip().lower() == "eletrica":
        mensagem_epi = "Obrigatório: luvas de alta tensão e botas dielétricas."
    elif str_setor.strip().lower() == "altura" or str_setor.strip().lower() == "trabalho em altura":
        mensagem_epi = "Obrigatório: cinturão de segurança e talabarte."

    msg_reciclagem, esta_em_dia = alerta_reciclagem(ano_treino_int)
    
    if esta_em_dia:
        total_em_dia += 1

    mensagem_final = f"Funcionário {str_nome} cadastrado!\n\nEPIs: {mensagem_epi}\n\nStatus Brigada: {msg_reciclagem}"
    messagebox.showinfo("Sucesso", mensagem_final)

    nome.delete(0,tk.END)
    setor.delete(0,tk.END)
    nr10.delete(0,tk.END)
    nr35.delete(0,tk.END)
    brigada.delete(0,tk.END)
    treino.delete(0,tk.END)

def relatorio():

    messagebox.showinfo("Relatório Geral", f"Total de funcionários cadastrados: {usuarios_cadastrado}\nFuncionários com treinamento em dia: {total_em_dia}")

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