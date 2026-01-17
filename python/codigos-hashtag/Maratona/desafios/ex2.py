M = int(input("Idade de dona Mônica: "))
A = int(input("Idade do filho A:"))
B = int(input("Idade do filho B: "))


C = M - (A+B)

if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
else:
    print(C)