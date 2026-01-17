#A Programação Orientada a Objetos se baseia em quatro pilares principais:

# Encapsulamento: agrupar dados e métodos em uma única unidade (objeto)
# Abstração: expor apenas o necessário e esconder a implementação
# Herança: criar novas classes a partir de classes existentes
# Polimorfismo: usar a mesma interface para diferentes tipos de objetos

# '''docstring()''' -> para documentar função da classe

#Classe
class Pessoa:
    apelido = "Gusta"

    # O método construtor é __init__ ; Self se refere a instância atual
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Método qualquer
    def saudacao(self):
        return f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos!"


# Instanciando a classe -> OBJETO
pessoa1 = Pessoa("Erick Gustavo", 18 )

print("\n ----Chamando método----")
print(pessoa1.saudacao())

print("\n ----Acessando atributos----")
print(pessoa1.apelido)
print(pessoa1.nome)

print("\n ----Modificando Atributos----")
pessoa1.nome = "Nome modificado"
print(pessoa1.nome)


    