#quantidade de lances
n = int(input())

maior_valor = 0
nome_vencedor = ""

for i in range(n):

    nome = str(input())
    valor = int(input())

    if valor > maior_valor:
        maior_valor = valor
        nome_vencedor = nome

print(nome_vencedor)
print(maior_valor)




