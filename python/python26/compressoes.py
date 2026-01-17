# List comprehensions permitem criar listas de forma concisa, combinando um loop for com uma expressão.



print("\n ----LISTS----")

# ---------- Quando Usar List Comprehensions  ---------- 
# Use list comprehensions quando precisar criar uma nova lista a partir de um iterável existente. Elas são mais 
# eficientes e legíveis do que loops for tradicionais para tarefas simples de transformação ou filtragem.

# [expressão(que vai ser retornada) for item in iterável]
# ou
# [expressão for item in iterável if condição]



# Lista com os quadrados dos números de 0 a 9
print([x**2 for x in range(10)])

# Lista com números pares até 10
print([x for x in range(11) if x % 2 == 0])

# Lista com comprimento de cada palavra
palavras = ["Python", "é", "incrível"]
print([len(p) for p in palavras])

# Lista com classificação(pa ou impar) de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(["par" if n % 2 == 0 else "impar" for n in numeros])


print("\n ----DICIONARIOS----")
# {chave_expressão: valor_expressão for item in iterável}
# ou
# {chave_expressão: valor_expressão for item in iterável if condição}

# Dicionário de número -> quadrado
print({x: x**2 for x in range(6)})

# Dicionário de palavra -> comprimento
palavras = ["Python", "é", "incrível"]
print({p: len(p) for p in palavras})

# Invertendo um dicionário (chave <-> valor)
pessoas = {"João": 25, "Maria": 30, "José": 35}
print({idade: nome for nome, idade in pessoas.items()})

# Convertendo todas as chaves para maiúsculas
frutas = {"maçã": "vermelha", "banana": "amarela", "uva": "roxa"}
print({nome.upper(): cor   for nome, cor in frutas.items()})