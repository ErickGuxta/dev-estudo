# Lista com os quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lista com números pares até 10
pares = [x for x in range(11) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10]

# Lista com comprimento de cada palavra
palavras = ["Python", "é", "incrível"]
comprimentos = [len(palavra) for palavra in palavras]
print(comprimentos)  # [6, 1, 9]