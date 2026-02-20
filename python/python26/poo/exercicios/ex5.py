from rich.traceback import install
install()

class Carro:

    

    def __init__(self, consumo: float, nivel_comb: float = 0):
        self.consumo = consumo  # km por litro
        self.nivel_comb = nivel_comb

    def adicionarGasolina(self, comb: float):
        self.nivel_comb = comb
        return f"Você abasteceu seu carro com: {self.nivel_comb:.2f} Litros"

    def andar(self, distancia: float):
        gasto_comb = distancia / self.consumo
        self.nivel_comb -= gasto_comb
        return f"Seu carro andou: {distancia:.2f} KM"

    def obterGasolina(self):
        return f"Quantidade atual no tanque: {self.nivel_comb:.2f} Litros"


if __name__ == "__main__":
    carro = Carro(consumo=10)
    print(carro.adicionarGasolina(50))
    print(carro.andar(100))
    print(carro.obterGasolina())
