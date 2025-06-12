a = int(input())  # mínimo leite
b = int(input())  # máximo leite
c = int(input())  # capacidade da xícara
d = int(input())  # CADA DOSE de café

possivel = False

doses_maximas = c // d  
# print(doses_maximas)

for doses in range(1, doses_maximas + 1):
    v_cafe = doses * d
    v_leite = c - v_cafe
    
    if a <= v_leite <= b:
        possivel = True
        break

if possivel:
    print('S')
else:
    print('N')