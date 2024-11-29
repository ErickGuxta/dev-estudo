# piloto automatico

A = int(input("Posição carro A: "))
B = int(input("Posição carro B: "))
C = int(input("Posição carro C: "))

if (B-A) < (C-B):
    print("1")
elif (B-A) > (C-B) :
    print("-1")
elif (B-A) == (C-B):
    print("0")
else:
    pass