n = int(input())
a = list(map(int, input().split())) # dinheiro que emprestou
b = list(map(int, input().split())) #dinheiro que pegou emprestao


receber = 0
pagar = 0

for i in range(n):
    if (a[i] > b[i]):
        receber += a[i] - b[i]
    elif (a[i] < b[i]):
        pagar += b[i] - a[i]

print(receber, pagar)