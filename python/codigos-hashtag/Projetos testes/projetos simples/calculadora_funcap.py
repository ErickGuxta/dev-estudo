def soma(n1, n2):
    s = n1 + n2
    return(s)


while True: 
    print("\nSelecione a operação:")
    print("1. Soma")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/5): ")


    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if escolha == "5":
        print("Obrigado! Adeus!")
        break

    if escolha == "1":
        print(soma(n1, n2))

import math

def adicionar(numeros):
    return sum(numeros)

def subtrair(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    try:
        for num in numeros[1:]:
            resultado /= num
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero"

def potencia(base, expoentes):
    resultado = base
    for exp in expoentes:
        resultado **= exp
    return resultado

def raiz_quadrada(numeros):
    try:
        return [math.sqrt(num) for num in numeros if num >= 0]
    except ValueError:
        return "Erro: Raiz quadrada de número negativo"

def mostrar_menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz quadrada")
    print("0. Sair")

def calcular():
    while True:
        mostrar_menu()
        escolha = input("Digite sua escolha (0/1/2/3/4/5/6): ")

        if escolha == '0':
            print("Saindo...")
            break

        if escolha in ['1', '2', '3', '4']:
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
        
        if escolha == '1':
            print(f"Resultado: {adicionar(numeros)}")
        elif escolha == '2':
            print(f"Resultado: {subtrair(numeros)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicar(numeros)}")
        elif escolha == '4':
            resultado = dividir(numeros)
            if resultado == "Erro: Divisão por zero":
                print(resultado)
            else:
                print(f"Resultado: {resultado}")
        elif escolha == '5':
            base = float(input("Digite a base: "))
            expoentes = list(map(float, input("Digite os expoentes separados por espaço: ").split()))
            print(f"Resultado: {potencia(base, expoentes)}")
        elif escolha == '6':
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
            resultado = raiz_quadrada(numeros)
            if "Erro" in resultado:
                print(resultado)
            else:
                print(f"Resultado: {resultado}")
        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__ == "__main__":
    calcular()


