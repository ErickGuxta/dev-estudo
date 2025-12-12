# ----- FOR -----

# interando sobre uma lista
frutas = ["maçã", "banana", "laranja"]

for i in frutas:
    print(f"{i}")
    
# interando sobre uma lista
palavra = "Python"

for i in palavra:
    print(f"{i}")

# ----- Função range() -----
# geralmente usada para gerar uma sequencia

# de 0 a 4
list01 = []
for i in range(5):
    list01.append(i)

#de 6 a 10
list02 = []
for i in range(2, 11):
    list02.append(i)
# de 1 a 9, incrementando de 2 em 2
list03 = []
for i in range(1, 10, 2):
    list03.append(i)

print(list01)
print(list02)
print(list03)

# ----- LOOP WHILE -----
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

# ----- LOOP DENTRO DE LOOP -----
#criando uma matriz 3 x 3
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(0)
    matriz.append(linha)

for i in matriz:
    print(i)


