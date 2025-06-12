n = int(input())  # quantidade de brinquedos
p = list(map(int, input().split()))  # quantidade de participantes

# maior valor dentro de p
h = max(p)

for i in range(h-1):  
    linha = ""
    for valor in p:
        if valor > i:
            linha += "1"
        else:
            linha += "0"
    print(linha)