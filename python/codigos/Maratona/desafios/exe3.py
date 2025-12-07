# divisão tesouro

A = int(input("numero moedas: "))
N = int(input("numero marinheiros: "))

def tesouro(A, N):

    x = A // (N + 2)   #moedas de cada marinheiro
    moeda_capitao = 2 * x
    return moeda_capitao

print(tesouro(A, N))






