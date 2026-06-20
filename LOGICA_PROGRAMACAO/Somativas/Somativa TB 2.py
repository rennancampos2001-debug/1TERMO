import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

# Exercicio 1

# def cadastrar_operador():
#     nome = ent_nome_usuario.get()
#     turno = cmb_qual_turno.get()

#     if nome == "" and turno == "":
#         messagebox.showwarning("Informações faltando", "Escreva seu nome e selecione seu turno !")
#     else:
#         messagebox.showinfo("Concluido", f"Operador {nome} registrado no turno {turno}. Boa jornada! ")

# janela = tk.Tk()
# janela.title("Registro do Operador")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Registro de Operadores",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_nome_usuario = tk.Label(janela,text="Qual é o seu nome ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_nome_usuario.grid(row=1, column=0,padx=10,pady=10)
# lbl_qual_turno = tk.Label(janela,text="Qual é o seu turno ?",font=("Arial", 14), fg="#FFFFFF", bg="#000000")
# lbl_qual_turno.grid(row=2, column=0,padx=10,pady=10)

# ent_nome_usuario = tk.Entry(janela,font=("Arial", 14),width=30,fg="#000000")
# ent_nome_usuario.grid(row=1,column=1,padx=10,pady=10)

# cmb_qual_turno = ttk.Combobox(janela, values=["A", "B", "C"], font=("Arial", 14),width=30, state="readonly")
# cmb_qual_turno.grid(row=2, column=1,padx=10,pady=10)

# btn_cadastrar = tk.Button(janela,text="Cadastrar",font=("Arial", 14),fg="#000000", bg="#00FF2A",command=cadastrar_operador)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 2

# def calculo_pecas():
#     pecas = int(ent_pecas_produzidas.get())

#     calculo = pecas * 8

#     if pecas =="":
#         messagebox.showwarning("Sem informações","Por favor coloque a quantidade de peças")
#     else:
#         messagebox.showinfo("Concluido", f"A quantidade de peças em 8 horas será de: {calculo}")

# janela = tk.Tk()
# janela.title("Calculo produção")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Calculo da produção",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_pacas_produzidas= tk.Label(janela,text="Quantas peças foram produzidas em 1 hora ?", font=("Arial",14),fg="#FFFFFF", bg="#000000")
# lbl_pacas_produzidas.grid(row=0,column=0,padx=10,pady=10)

# ent_pecas_produzidas= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_pecas_produzidas.grid(row=0, column=1,padx=10,pady=10)

# btn_cadastrar= tk.Button(janela, text="Calcular", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=calculo_pecas)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 3

# def calculo_bar():
#     pressao_bar = ent_pressao_bar.get()

#     pressao_psi = float(pressao_bar) * 14.5

#     if pressao_bar == "":
#         messagebox.showwarning("Incompleto", "Coloco o valor da pressão")
#     else:
#         messagebox.showinfo("Concluido", f"A pressão em PSI é de: {pressao_psi:.2f}")

# janela = tk.Tk()
# janela.title("Calculo PSI")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Calculo de Bar para PSI",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_pressao_bar= tk.Label(janela,text="Qual é a pressão em Bar ?", font=("Arial",14),fg="#FFFFFF", bg="#000000")
# lbl_pressao_bar.grid(row=1,column=0,padx=10,pady=10)

# ent_pressao_bar= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_pressao_bar.grid(row=1, column=1,padx=10,pady=10)

# btn_cadastrar= tk.Button(janela, text="Calcular", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=calculo_bar)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 4

# def media_qualidade():
#     peca_1 = int(ent_peca_1.get())
#     peca_2 = int(ent_peca_2.get())
#     peca_3 = int(ent_peca_3.get())

#     media = peca_1+peca_2+peca_3 / 3

#     if peca_1 == "" and peca_2 == "" and peca_3 == "":
#         messagebox.showwarning("Incompleto", "Por favor digite a nota das peças !")
#     else:
#         messagebox.showinfo("Calculado", f"A media de nota das peças é de: {media}")
# janela = tk.Tk()
# janela.title("Media")
# janela.geometry("600x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Nota das Peças",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_peca_1= tk.Label(janela,text="Peça 1", font=("Arial",14),fg="#FFFFFF", bg="#000000")
# lbl_peca_1.grid(row=1,column=0,padx=10,pady=10)
# lbl_peca_2= tk.Label(janela,text="Peça 2", font=("Arial",14),fg="#FFFFFF", bg="#000000")
# lbl_peca_2.grid(row=2,column=0,padx=10,pady=10)
# lbl_peca_3= tk.Label(janela,text="Peça 3", font=("Arial",14),fg="#FFFFFF", bg="#000000")
# lbl_peca_3.grid(row=3,column=0,padx=10,pady=10)

# ent_peca_1= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_peca_1.grid(row=1,column=1,padx=10,pady=10)
# ent_peca_2= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_peca_2.grid(row=2, column=1,padx=10,pady=10)
# ent_peca_3= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_peca_3.grid(row=3,column=1,padx=10,pady=10)

# btn_cadastrar= tk.Button(janela, text="Média", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=media_qualidade)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 5

# def temperatura_motor():
#     temperatura = int(ent_temperatura.get())

#     if temperatura == "":
#         messagebox.showwarning("Incompleto", "Qual a temperatura do motor ?")
#     elif temperatura >= 40:
#         messagebox.showinfo("Completo", "O motor está com baixa carga")
#     elif temperatura >= 70:
#         messagebox.showinfo("Completo", "O motor está normal")
#     else:
#         messagebox.showwarning("Completo", "ALERTA: Resfriamento ativado")


# janela = tk.Tk()
# janela.title("temperatuta")
# janela.geometry("600x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Termostato inteligente",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_temperatura= tk.Label(janela,text="Qual a temperatura do motor",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_temperatura.grid(row=1,column=0,padx=10,pady=10)

# ent_temperatura= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_temperatura.grid(row=1,column=1,padx=10,pady=10)

# btn_cadastrar= tk.Button(janela, text="Verificar", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=temperatura_motor)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 6

# def verificar_alimento():
#     codigo = ent_codigo_produto.get().strip().upper()

#     if codigo == "":
#         messagebox.showwarning("Vazio", "Por favor, coloque um codigo")
#     elif codigo.startswith("A"):
#         messagebox.showinfo("Concluido","O produto é um: Alimento")
#     elif codigo.startswith("E"):
#         messagebox.showinfo("Concluido","O produto é um: Eletrônico")
#     else:
#         messagebox.showinfo("Não indentificado", "O produto é desconhecido")

# janela = tk.Tk()
# janela.title("Classificador")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Classificador de lotes",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_codigo_produto= tk.Label(janela,text="Qual é o codígo ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_codigo_produto.grid(row=1,column=0,padx=10,pady=10)

# ent_codigo_produto= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_codigo_produto.grid(row=1,column=1,padx=10,pady=10)


# btn_cadastrar= tk.Button(janela, text="verificar", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=verificar_alimento)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 7

# def sistema_operacional():
#     sensor_porta = cmb_porta_maquina.get()
#     botão_Emergencia = cmb_emergencia_botão.get()

#     if sensor_porta == "Fechada" and botão_Emergencia == "Desligado":
#         messagebox.showinfo("Liberado", "A maquna pode ser iniciada")
#     else:
#         messagebox.showinfo("desabilitada", "A operação não pode ser continuada")

# janela = tk.Tk()
# janela.title("Segurança operacional")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Aprovação de ativação",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_porta_sensor= tk.Label(janela,text="A porta está fechada ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_porta_sensor.grid(row=1,column=0,padx=10,pady=10)
# lbl_emergencia_botao= tk.Label(janela,text="Qual é o codígo ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_emergencia_botao.grid(row=2,column=0,padx=10,pady=10)

# cmb_porta_maquina= ttk.Combobox(janela, values=["Aberta", "Fechada"],font=("Arial", 14),width=30, state="readonly")
# cmb_porta_maquina.grid(row=1, column=1,padx=10,pady=10)
# cmb_emergencia_botão= ttk.Combobox(janela, values=["Ligado", "Desligado"],font=("Arial", 14),width=30, state="readonly")
# cmb_emergencia_botão.grid(row=2, column=1,padx=10,pady=10)

# btn_cadastrar= tk.Button(janela, text="Ativar", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=sistema_operacional)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 8

# def calculo_descarte():

#     pecas_totais = int(ent_pecas_total.get())
#     pecas_defeito = int(ent_pecas_defeito.get())

#     if pecas_defeito >= pecas_totais * 0.05:
#         messagebox.showinfo("desqualificado","O processo precisa ser revisado")
#     else:
#         messagebox.showinfo("qualificado","O processo esta otimizado")

# janela = tk.Tk()
# janela.title("Descarte")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Calcular descarte",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_pecas_totais= tk.Label(janela,text="Quantas peças foram produzidas ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_pecas_totais.grid(row=1,column=0,padx=10,pady=10)
# lbl_pecas_defeito= tk.Label(janela,text="Quantas peças sairam defeituosas ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_pecas_defeito.grid(row=2,column=0,padx=10,pady=10)

# ent_pecas_total= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_pecas_total.grid(row=1,column=1,padx=10,pady=10)
# ent_pecas_defeito= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_pecas_defeito.grid(row=2,column=1,padx=10,pady=10)


# btn_cadastrar= tk.Button(janela, text="calcular", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=calculo_descarte)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 9

# def verificar_medida():
#     medida = float(ent_medida_peca.get())

#     if medida == 0:
#         messagebox.showwarning("Invalido","Insira uma medida")
#     elif medida >= 9.8 and medida<=10.2:
#         messagebox.showinfo("Correto","A peça está dentro da tolerancia")
#     else:
#         messagebox.showinfo("Errado","A peça está fora da tolerancia")

# janela = tk.Tk()
# janela.title("Classificador")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# lbl_titulo= tk.Label(janela,text="Validação da peça",font=("Arial", 18),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)
# lbl_codigo_produto= tk.Label(janela,text="Qual foi a medida da peça ?",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_codigo_produto.grid(row=1,column=0,padx=10,pady=10)

# ent_medida_peca= tk.Entry(janela,font=("Arial",14),width=30,fg="#000000")
# ent_medida_peca.grid(row=1,column=1,padx=10,pady=10)


# btn_cadastrar= tk.Button(janela, text="Tolerancia", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=verificar_medida)
# btn_cadastrar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 10

# janela = tk.Tk()
# janela.title("Classificador")
# janela.geometry("900x400")
# janela.configure(bg="Black")

# def inicio():
#     tempo = 10

#     for tempo in range(10,0,-1):
#         messagebox.showinfo("Iniciado",f"tempo: {tempo}")
#         tempo -= 1

#     if tempo == 0:
#         messagebox.showinfo("Ativada", "A prensa foi ativa")

# lbl_titulo=tk.Label (janela,text="Iniciar contagem regressiva",font=("Arial", 14),fg="#FFFFFF",bg="#000000")
# lbl_titulo.grid(row=0,column=1,padx=10,pady=10)

# btn_iniciar= tk.Button(janela, text="Iniciar", font=("Arial", 14),fg="#000000",bg="#00FF2A", command=inicio)
# btn_iniciar.grid(row=5,column=1,padx=10,pady=10)
# btn_sair = tk.Button(janela,text="Sair",font=("Arial", 14),fg="#000000", bg="#FF0000", command=janela.destroy)
# btn_sair.grid(row=6, column=1,padx=10,pady=10,)

# janela.mainloop()

# Exercicio 11

# root = tk.Tk()
# root.withdraw()

# peso_total = 0.0

# while True:

#     peso = simpledialog.askfloat("Entrada", "Digite o peso da caixa (ou 0 para sair):")
    
#     if peso == 0 or peso is None:
#         break
        
#     peso_total += peso

# messagebox.showinfo("Resultado", f"O peso total acumulado é: {peso_total:.2f} kg")

# Exercicio 12

# from tkinter import *
# from tkinter import simpledialog, messagebox

# janela = Tk()
# janela.withdraw()  

# maior = float("-inf")

# for i in range(1, 6):
#     temperatura = float(simpledialog.askstring(
#         "Sensor",
#         f"Digite a temperatura do sensor {i}:"
#     ))

#     if temperatura > maior:
#         maior = temperatura

# messagebox.showinfo("Resultado", f"A maior temperatura foi: {maior}°C")

# exercicio 13

# from tkinter import *

# senha_correta = "admin123"
# tentativas = 0

# def verificar():
#     global tentativas

#     senha = entrada.get()

#     if senha == senha_correta:
#         resultado.config(text="Acesso Permitido", fg="green")
#         botao.config(state=DISABLED)
#     else:
#         tentativas += 1

#         if tentativas < 3:
#             resultado.config(text="Acesso Negado", fg="red")
#             entrada.delete(0, END)
#         else:
#             resultado.config(text="Painel Bloqueado", fg="red")
#             botao.config(state=DISABLED)
#             entrada.config(state=DISABLED)

# janela = Tk()
# janela.title("Painel de Login")

# Label(janela, text="Digite a senha:").pack()

# entrada = Entry(janela, show="*")
# entrada.pack()

# botao = Button(janela, text="Entrar", command=verificar)
# botao.pack()

# resultado = Label(janela, text="")
# resultado.pack()

# janela.mainloop()