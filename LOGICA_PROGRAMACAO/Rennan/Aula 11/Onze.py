def nome():
    nome = input("Digite seu nome ")
    return nome
print(f"Olá, {nome()}!")

def valores():
    print("Digite três valores:")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor?: "))
    c = int(input("Digite o terceirp valor: "))
    return a, b, c

print(f"O maior valor é: {max(valores())}")
# reutilizando valores
nome()
valores() 

## Conceitos Chave
# def: Indica o início da definição da função.
# Nome: Indentifica a função para você chamá-la depois.
# Parâmetros: Dados que a função recebe (opcional).
# Return: Envia o resultado de volta para quem chamou a função (opcional).
def calcular_dobro(numero):
    return numero * 2
# Como usar:resultado = calcular_dobro(5)
print(calcular_dobro(5))    