from collections import deque

def pessoa_e_vendedor(nome):
      return nome[-1] == 'm'

# o grafo é representado como um dicionário (dict)
# Usando o construtor dict()
# dicionario = dict(chave1='valor1', chave2='valor2', chave3='valor3')

# Acessando valores
# print(dicionario['chave1'])  # Output: valor1

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["leom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def pesquise(nome):
    fila_de_pesquisa = deque()  #deque é uma estrutura de dados que permite a inserção e a remoção de elementos 
    fila_de_pesquisa += [nome]  #tanto no início quanto no final da fila de forma eficiente.
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft() #popleft() Remove o elemento do início
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é o vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += graph[pessoa]
                verificadas.append(pessoa)

    return False

pesquise("you")