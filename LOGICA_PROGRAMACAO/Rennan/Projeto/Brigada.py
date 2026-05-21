def cadastro():
    nome = input("For favor informe seu nome: ")
    setor = input(f"ok {nome}, qual é seu setor? ")
    status = input("Ótimo, e qual seu status de treinamento? ")
    return nome, setor, status  # Apenas devolve os dados

entrada = input("Seja bem vindo ao SESMT, você deseja entrar? ")

if entrada == "Sim":
    # AQUI É A MÁGICA: você chama a função e guarda os resultados
    nome, setor, status = cadastro() 
    
    if setor == "Elétrica":
        print(f"{nome},  Solicitamos o uso obrigatorio de EPI seguidamente ditas: luvas de alta tensão, botas dielétricas, Uniforme ATPV, Óculos de Segurança e Capacete de Segurança.")
    elif setor == "Trabalho em Altura":
        print(f"{nome}, Solicitamos o uso obrigatorio de EPI seguidamente ditas: o cinturão de segurança, talabarte, Capacete, e a retirada de todas as partes metalicas de exposição ou que sejam isoladas. ")

int(input("Qual foi o ano que você fez o seu treinamento? "))
    