n, m = map(int, input().split())

calorias_consumidas = 0
for _ in range(n):
    p, g, c = map(int, input().split())
    calorias_consumidas += (p * 4) + (g * 9) + (c * 4)

if calorias_consumidas <= m:
    print(m - calorias_consumidas)  
else:
    print(0)  

