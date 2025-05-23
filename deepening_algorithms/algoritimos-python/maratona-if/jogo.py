p, d1, d2 = int(input()), int(input()), int(input())

soma = d1 + d2 

if p == 0:
    if soma % 2 == 0:
        print(0)
    else:
        print(1)
elif p == 1:
    if soma % 2 == 0:
        print(1)
    else:
        print(0)
