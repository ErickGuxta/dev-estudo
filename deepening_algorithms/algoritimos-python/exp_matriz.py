(n, m )= map(int, input().split())

matriz = []

cont = 1
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(cont)
        cont +=1
    matriz.append(linha)


for linha in matriz:
    print(linha)