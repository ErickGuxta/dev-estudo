print("Hello word")

# nome = input("Digite seu nome: ")
# idade =  int(input("Digite sua idade"))
# peso =  float(input("Digite seu peso"))

# print(nome)
# print(idade)
# print(peso)


# FOR

# #usando range
# produtos = ['coca', 'pepsi', 'guarana', 'sprite']

# tamanho = len(produtos)

# for i in range(tamanho):
#     print(produtos[i])

# #usando enumerate (retorna o índice e o valor do item)

# for i, produto in enumerate(produtos):
#     print(i, produto)


notas= []

for i in range(2):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado =  [codigo_aluno, nota]
    notas.append(resultado)

print(notas)
print("Quantidade de notas", len(notas))

for x in notas:
    codigo_aluno = x[0]
    notas = x[1]
    print("O RM" , codigo_aluno, "Tirou a nota: ", nota)
