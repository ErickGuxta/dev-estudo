#Definindo funções

def saudacao():
    print("olá, Erick!!")

saudacao()

#Parâmetros

def saudacao2(nome, mensagem= "olá"):
    return f"{mensagem}, {nome}"

print(saudacao2("Maria", "oi"))

#FUNÇÕES LAMBDA
"Elas podem ter qualquer número de argumentos, mas apenas uma expressão."

quadrado = lambda x: x**2
print(quadrado(5))

# Usando com filter()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Usando com map()
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# FUNÇÕES INTEGRADAS
# len() - comprimento de um objeto
print(len("Python"))  # Saída: 6

# range() - sequência de números
lista = list(range(1, 6))
print(lista)  # Saída: [1, 2, 3, 4, 5]

# type() - tipo do objeto
print(type(123))      # Saída: <class 'int'>
print(type("texto"))  # Saída: <class 'str'>

# map() - aplica função a cada item de um iterável
numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16]

# filter() - filtra itens por uma função
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]

# sorted() - retorna lista ordenada
frutas = ["banana", "maçã", "laranja"]
ordenadas = sorted(frutas)
print(ordenadas)  # Saída: ['banana', 'laranja', 'maçã']