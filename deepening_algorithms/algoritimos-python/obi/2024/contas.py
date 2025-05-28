valor = int(input())

#contas
a = int(input())
f = int(input())
p = int(input())

contas = [a, f, p]
contas_sort = sorted(contas)

pagas = 0

if contas_sort[2] + contas_sort[1] + contas_sort[0] <= valor:
    pagas = 3
elif contas_sort[1] + contas_sort[0] <= valor:
    pagas = 2
elif contas_sort[0] <= valor:
    pagas = 1

print(pagas)