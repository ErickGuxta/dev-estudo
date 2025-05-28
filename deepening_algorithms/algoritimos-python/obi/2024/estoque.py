#tipos(linhas) e tamanhos(colunas)
m, n = map(int, input().split())



estoque = []
pecas_vendidas = 0


for i in range(m):
    linha = list(map(int, input().split()))  
    estoque.append(linha)
    
#pedidos
p = int(input())

for _ in range(p):
    i, j = map(int, input().split())

    if estoque[i-1][j-1] > 0:
        estoque[i-1][j-1] -= 1
        pecas_vendidas += 1

print(pecas_vendidas)
