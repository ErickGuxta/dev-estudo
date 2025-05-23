k, n = map(int, input().split())

alfabeto = str(input())
mensagem = str(input())

resposta = "S"
for i in mensagem:
    if not i in alfabeto:
        resposta = "N"
        break

print(resposta)