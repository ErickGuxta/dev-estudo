from logging import info


class Node:
    def __init__(self, value):
        self.value = value
        self.proximo = None

# Criando nós
carro = Node(2)
novo_no = Node(6)


# Ligando os nós
carro.proximo = novo_no

print(carro.value)
print(carro.proximo.value)  # Imprime 2