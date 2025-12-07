N = int(input(""))

A = 0
B = 0


for i in range(N):
    apertar = int(input(""))

    if apertar == 1:
        A = 1 - A
    elif apertar == 2:
        A = 1 - A
        B = 1 - B

print(f"Saida: A = {A}, B = {B}")


