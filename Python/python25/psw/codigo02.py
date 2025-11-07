a = int(input("A:"))
b = int(input("B:"))

if a > b:
    print("A é maior que B")
elif b > a:
    print("B é maior que A")
else:
    print("A e B são iguais")

print("A é maior" if a > b else "A não é maior")
