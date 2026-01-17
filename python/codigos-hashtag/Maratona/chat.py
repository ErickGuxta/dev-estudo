import os

mensagens = []

nome = input("Nome:")


while True:

    os.system('cls')

    if len(mensagens) > 0:
        for mensagem in mensagens:
            print(mensagem['nome'], "-", mensagem['texto'])
    

    print("__________________")

    texto = input("Texto:")

    if texto == "fim chat":
        break

    mensagens.append({
        'nome': nome,
        'texto': texto
    })

