# métodos de listas
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
## ordenação
numeros.sort()                 # [1, 1, 2, 3, 4, 5, 6, 9]
numeros.sort(reverse=True)     # [9, 6, 5, 4, 3, 2, 1, 1]

## Não modifica a lista original
ordenada = sorted(numeros)     # Retorna uma nova lista ordenada

## Invertendo
numeros.reverse()              # Inverte a ordem dos elementos

## Contagem e localização
contagem = numeros.count(1)    # Retorna quantas vezes 1 aparece
indice = numeros.index(5)      # Retorna o índice da primeira ocorrência de 5

## Comprimento
tamanho = len(numeros)         # Retorna o número de elementos na lista


# --- COMPREENSAO DE LISTA ---
## criando uma lista de quadrados dos numeros de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

## criando uma matriz 3x3
matriz = [[i + j + 1 for j in range(3)] for i in range(4)]
print(matriz)