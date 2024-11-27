# Definindo o vetor e a chave a ser buscada
vetor = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
chave = 2

# Inicializando os índices de começo e fim
comeco = 0
fim = len(vetor) - 1

encontrado = False

# Executando a busca binária
while comeco <= fim:
    meio = (comeco + fim) // 2
    
    if vetor[meio] == chave:
        print(f"A chave {chave} foi encontrada na posição {meio}.")
        encontrado = True
        break
    elif vetor[meio] < chave:
        comeco = meio + 1
    else:
        fim = meio - 1

if not encontrado:
    print(f"A chave {chave} não foi encontrada no vetor.")