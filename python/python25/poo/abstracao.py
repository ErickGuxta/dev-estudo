# Abstração: expor apenas o necessário e esconder a implementação
    # criando moldes para construir classes (molde do molde)

    
print("\n ----ABSTRAÇÃO----")
# Abstract Base Class - Classe Base Abstrata
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "carro ligado"

    def desligar(self):
        return "carro desligado"


corolla = Carro()

print(corolla.ligar())
print(corolla.desligar())