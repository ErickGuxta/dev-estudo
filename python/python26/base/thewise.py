class Carro:

    def __init__(self, cor, n_porta, modelo, ano):
        self.cor = cor
        self.n_porta = n_porta
        self.__modelo = modelo
        self.ano = ano
    
    def andar(self):
        print(f"O carro da cor: {self.cor} está andando!")
    
    def abrir_porta(self):
        print(f"O carro da cor: {self.cor} está com as {self.n_porta} abertas!")

meu_carro = Carro("vermelho", "4", "golf", "2010")

meu_carro.andar()
meu_carro.abrir_porta()

print(meu_carro.    modelo)