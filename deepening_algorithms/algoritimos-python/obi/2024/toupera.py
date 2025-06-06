s, t = map(int, input().split())

tuneis = set()
for _ in range(t):
    x, y = map(int, input().split())
    tuneis.add((x, y))
    tuneis.add((y, x))  # Adiciona o túnel nas duas direções

p = int(input())

total = 0
for _ in range(p):
    passeio = list(map(int, input().split()))
    saloes = passeio[1:]  # saloes. usei 1: para fatiar, ou seja, começa pegando a partir do segundo elemento
    
    #passeio[0] é a quantidade de saloes (N)
    ok = True
    for i in range(len(saloes) - 1):
        if (saloes[i], saloes[i + 1]) not in tuneis:
            ok = False
            break
    if ok:
        total += 1

print(total)