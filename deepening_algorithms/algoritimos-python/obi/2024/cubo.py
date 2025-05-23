n = int(input());

if n == 2:
    resposta = [0, 0, 0, 8]
else:
    resposta = [
        (n-2)*(n-2)*(n-2),
        (n-2)*(n-2)*6,
        (n-2)*12,
        8
    ]

for i in resposta:
    print(i);