n = int(input())

divisores = 0

for x in range (1, n+1):
    if n % x == 0:
        divisores += 1

print(divisores)