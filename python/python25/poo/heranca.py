print("\n ----HERANÇA----")

class Animal:
    def __init__(self, nome) ->None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return

    def emitir_som(self):
        pass

'''classe herdada de Animal'''
class Cachorro(Animal):
    def emitir_som(self):
        return "au au au"


class Gato(Animal):
    def emitir_som(self):
        return "miau miau miau"  

# Instanciando
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\n ----Exemplo Polimorfismo----")
animais = [dog,cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

