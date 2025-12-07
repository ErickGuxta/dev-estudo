while True:
    print("\nSelecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha == '5':
        print("Obrigado por usar a calculadora. Adeus!")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida. Por favor, escolha novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", num1 + num2)
    elif escolha == '2':
        print("Resultado:", num1 - num2)
    elif escolha == '3':
        print("Resultado:", num1 * num2)
    elif escolha == '4':
        if num2 == 0:
            print("Erro: Divisão por zero!")
        else:
            print("Resultado:", num1 / num2)
