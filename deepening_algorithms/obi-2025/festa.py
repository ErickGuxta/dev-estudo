e = int(input())
s = int(input())
l = int(input())

soma1 = abs(e - s) + abs(s - l) + abs(l - e)

soma2 = abs(e - l) + abs(l - s) + abs(s - e)

print(min(soma1, soma2))