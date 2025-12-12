print("\n ----HERANÇA----")

class Animal:
    def __init__(self, nome, idade) ->None:
        self.nome = nome
        self.idade = idade

    def andar(self):
        print(f"O animal {self.nome} andou")
        return

    def emitir_som(self):
        pass

'''classe herdada de Animal'''
class Cachorro(Animal):

    # chamando o construtor da classe pai
    def __init__(self, nome, idade, raca):
        # O método super() é usado para chamar métodos da classe pai, o que é essencial para 
        # a extensão(acrescentar mais coisa) de comportamentos em subclasses.
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "au au au"

class Gato(Animal):

    def __init__(self, nome, idade, raca):
        # chamando o construtor da classe pai
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "miau miau miau"  


# Instanciando
dog = Cachorro(nome="Rex", idade = 1, raca = "pitbull")
cat = Gato(nome="Felix", idade = 2, raca = "persa")

print("\n ----Exemplo Polimorfismo----")
animais = [dog,cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

