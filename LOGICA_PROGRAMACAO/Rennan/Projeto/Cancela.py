import time
import math

TOTAL_VAGAS = 500
VAGAS_RESERVADAS_TAG = 50
VAGAS_COMUNS = TOTAL_VAGAS - VAGAS_RESERVADAS_TAG

vagas_ocupadas = 0
carros = {}

while True:
    print("\n=== ESTACIONAMENTO SHOPPING ===")
    print("Vagas disponíveis:", TOTAL_VAGAS - vagas_ocupadas)

    acao = input("\nENTRADA / SAIDA / SAIR: ").lower()

    if acao == "sair":
        print("Sistema encerrado.")
        break

    if acao == "entrada":

        placa = input("Placa do veículo: ").upper()
        tipo = input("Tipo (TAG/TICKET): ").lower()

        if tipo == "tag":
            if vagas_ocupadas >= TOTAL_VAGAS:
                print("Estacionamento lotado, mas TAG ainda pode entrar.")

            ativa = input("TAG ativa? (sim/nao): ").lower()

            if ativa == "sim":
                carros[placa] = [time.time(), "tag", "pendente"]
                vagas_ocupadas += 1
                print("Entrada liberada via TAG.")
            else:
                print("TAG inativa. Entrada negada.")

        elif tipo == "ticket":

            if vagas_ocupadas >= TOTAL_VAGAS:
                print("Estacionamento lotado. Entrada negada.")

            elif vagas_ocupadas >= VAGAS_COMUNS:
                print("Vagas comuns lotadas. Apenas TAGs podem entrar.")

            else:
                carros[placa] = [time.time(), "ticket", "pendente"]
                vagas_ocupadas += 1
                print("Ticket emitido. Entrada liberada.")

        else:
            print("Tipo inválido.")

    elif acao == "saida":

        placa = input("Placa do veículo: ").upper()

        if placa not in carros:
            print("Registro não encontrado.")
            print("Taxa de perda de ticket: R$ 50.00")
            continue

        entrada_time, tipo, status = carros[placa]
        saida_time = time.time()
        minutos = (saida_time - entrada_time) / 60

        if minutos <= 15:
            valor = 0
        elif minutos <= 180:
            valor = 15
        else:
            extras = math.ceil((minutos - 180) / 60)
            valor = 15 + (extras * 3)

        if tipo == "tag":
            valor *= 0.9

        print(f"\nTempo total: {minutos:.1f} minutos")
        print(f"Valor a pagar: R$ {valor:.2f}")

        pagamento = input("Pagamento realizado? (sim/nao): ").lower()

        if pagamento == "sim":
            carros[placa][2] = "pago"
            print("Pagamento confirmado. Cancela liberada.")
            del carros[placa]
            vagas_ocupadas -= 1
        else:
            print("Pagamento pendente. Saída bloqueada.")

    else:
        print("Opção inválida.")

    if TOTAL_VAGAS - vagas_ocupadas <= 10:
        print("ESTACIONAMENTO QUASE LOTADO!")