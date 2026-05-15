funcionarios = []


def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor (Elétrica/Trabalho em Altura): ")

    nr10 = input("Possui treinamento NR-10? (sim/não): ")
    nr35 = input("Possui treinamento NR-35? (sim/não): ")
    brigada = input("Possui treinamento de Brigada? (sim/não): ")

    funcionario = {
        "nome": nome,
        "setor": setor,
        "nr10": nr10,
        "nr35": nr35,
        "brigada": brigada
    }

    return funcionario


def verificar_epi(setor):

    if setor.lower() == "elétrica":
        print("\nEPIs obrigatórios:")
        print("- Luvas de alta tensão")
        print("- Botas dielétricas")

    elif setor.lower() == "trabalho em altura":
        print("\nEPIs obrigatórios:")
        print("- Cinturão de segurança")
        print("- Talabarte")

    else:
        print("\nSetor não identificado.")


def verificar_reciclagem(ano):

    ano_atual = 2026

    if ano_atual - ano > 2:
        print("Treinamento Vencido! Encaminhar para reciclagem.")

    else:
        print("Treinamento Válido.")


while True:

    resposta = input("\nDeseja cadastrar um funcionário? (sim/não): ").strip().lower()

    if resposta == "sim":

        dados = cadastrar_funcionario()

        funcionarios.append(dados)

        verificar_epi(dados["setor"])

        ano = int(input("Digite o ano do último treinamento da Brigada: "))

        verificar_reciclagem(ano)

    else:
        break


total = len(funcionarios)
em_dia = 0

for f in funcionarios:

    if (
        f["nr10"].lower() == "sim"
        and f["nr35"].lower() == "sim"
        and f["brigada"].lower() == "sim"
    ):

        em_dia += 1


print("\n===== RELATÓRIO GERAL =====")
print(f"Total de funcionários cadastrados: {total}")
print(f"Funcionários com treinamentos em dia: {em_dia}")