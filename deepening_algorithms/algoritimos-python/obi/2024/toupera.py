s, t = map(int, input().split())

tuneis = []
for _ in range(t):
    x, y = map(int, input().split())
    tuneis.append((x, y))
    tuneis.append((y, x))  # Adiciona o túnel nas duas direções

p = int(input())

possiveis = 0
for _ in range(p):
    passeio = list(map(int, input().split()))
    n = passeio[0] #numero de saloes
    saloes = passeio[1:] # saloes. usei 1: para fatiar, ou seja, começa pegando a partir do segundo elemento
    
    valido = True
    for i in range(n - 1):
        atual = saloes[i]
        proximo = saloes[i + 1]
        if (atual, proximo) not in tuneis:
            valido = False
            break
    
    if valido:
        possiveis += 1

print(possiveis)