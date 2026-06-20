# Atividade 1

# nome = input("Qual é o seu nome ? ")
# turno = input("você faz parte do turno A, B ou C ? ")

# print(f"Operador {nome} registrado no Turno {turno}. Boa jornada!")

# Atividade 2 

# pecas_hora = int(input("Quantas peças foram produzidas em 1 hora ? "))

# calculo = pecas_hora * 8

# print(f"A quantidade de peças em 8 horas será de: {calculo}")

# Atividade 3

# pressao_bar = float(input("Qual a pressão em  Bar : "))

# conversao = pressao_bar * 14.5

# print(f"A pressão em PSI é de: {conversao}")

# Atividade 4

# nota1 = float(input("Qual é a primeira nota: "))
# nota2 = float(input("Qual é a segunda nota: "))
# nota3 = float(input("Qual é a terceira nota: "))

# media = nota1 + nota2 + nota3 / 3

# print(f"A media das notas é de: {media:.2f}")

# Atividade 5 

# temperatura = float(input("Qual é a temperatura do motor ? "))

# if temperatura < 40:
#     print("Baixa carga")
# elif temperatura <= 70:
#     print("Normal")
# else:
#     print("Alerta:Resfriamento Ativado!")

# Atividade 6 

# codigo = input("Qual é o código do produto? ").upper()

# if codigo.startswith("A"):
#     print("Alimentos")
# elif codigo.startswith("E"):
#     print("Eletrônicos")
# else:
#     print("Desconhecido")

# Atividade 7

# porta = input("A porta está fechada ? (Sim/Não) ").lower()
# botao = input("O botão de emergencia esta ligado ? (Sim/Não) ").lower()

# if porta == "sim" and botao == "nao":
#     print("Maquina iniciada")
# else:
#     print("A maquina não pode seer iniciada")

# Atividade 8

# pecas_totais = int(input("Qual foi a quantidade de peças fabricadas hoje ? "))
# pecas_defeito = int(input("Quantas peças sairam defeituosas ? "))

# descarte = (pecas_defeito/pecas_totais) * 100

# if descarte >= 5:
#     print("O processo precisa ser revisado")
# else:
#     print("O processo esta otimizado")

# Atividade 9

# medida = float(input("Qual a medida da peça ? "))

# if medida >= 9.8 and medida <= 10.2:
#     print("A peça esta dentro da tolerancia")
# else:
#     print("A peça esta fora da tolerancia")

# Atividade 10

# for tempo in range(10, 0, -1):
#     print(tempo)

# print("Prensa ativa ! ")

# Atividade 11

# total = 0

# peso = float(input("Qual é o peso da caixa ? (0 para parar) "))

# while peso != 0:
#     total = total + peso
#     peso = float(input("Qual é o peso da caixa ? (0 para parar) "))

# print(f"O peso total das caixas é de: {total:.2f}")

# Atividade 12

# maior = float("-inf")

# for i in range(5):
#     temperatura = float(input("Digite a temperatura do sensor: "))

#     if temperatura > maior:
#         maior = temperatura

# print("Maior temperatura lida:", maior)

# Atividade 13

# senha_correta = "admin123"
# tentativas = 0

# while tentativas < 3:
#     senha = input("Digite a senha do supervisor: ")

#     if senha == senha_correta:
#         print("Acesso Liberado")
#         break
#     else:
#         print("Acesso Negado")
#         tentativas += 1

# if tentativas == 3:
#     print("Painel Bloqueado")

# Atividade 14

# estoque = 100

# while True:
#     print("\nMENU")
#     print("1 - Adicionar itens")
#     print("2 - Remover itens")
#     print("3 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         quantidade = int(input("Quantidade para adicionar: "))
#         estoque += quantidade

#     elif opcao == "2":
#         quantidade = int(input("Quantidade para remover: "))
#         estoque -= quantidade

#     elif opcao == "3":
#         print("Encerrando sistema...")
#         break

#     else:
#         print("Opção inválida!")

#     if estoque < 10:
#         print("Estoque Crítico!")

    # print("Estoque atual:", estoque)

# Atividade 15

# aprovadas = 0

# for i in range(5):
#     diametro = float(input("Digite o diâmetro da peça: "))

#     if 19.9 <= diametro <= 20.1:
#         aprovadas += 1

# eficiencia = (aprovadas / 5) * 100

# print("Peças aprovadas:", aprovadas)
# print("Eficiência do lote:", eficiencia, "%")