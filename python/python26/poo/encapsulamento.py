#A Programação Orientada a Objetos se baseia em quatro pilares principais:

# Encapsulamento: agrupar dados e métodos em uma única unidade (objeto)
# Abstração: expor apenas o necessário e esconder a implementação
# Herança: criar novas classes a partir de classes existentes
# Polimorfismo: usar a mesma interface para diferentes tipos de objetos

# '''docstring()''' -> para documentar função da classe

print("\n ----ENCAPSULAMENTO EXEMPLO 1----")

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Método PÚBLICO    
    def saudacao(self):
        return f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos!"

    # Método PRIVADO (utilitário)
    def _metodo_privado(self):
        self.mensagem = 'tudo ok'
        return self.mensagem

    # para acessar metodo privado:
    def get_metodo_privado(self):
        print(self._metodo_privado())


p1 = Pessoa("Erick Gustavo", 18 )
p1.get_metodo_privado()


print("\n ----ENCAPSULAMENTO EXEMPLO 2----")

'''criando uma classe com atributos e métodos PRIVADOS (__var)'''
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

print("\n ----chamando métodos----")

conta1 = ContaBancaria(1000)
conta1. depositar(125)
print(f"Saldo atual: {conta1.consultar_saldo()}")
conta1. depositar(209)
print(f"Saldo atual: {conta1.consultar_saldo()}")
conta1.sacar(900)


#print(conta1.__saldo) #ERROR
print(f"Saldo atual: {conta1.consultar_saldo()}")


    
    