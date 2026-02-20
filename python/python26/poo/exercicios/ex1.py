from rich.traceback import install
install()

lA, lB, lC = map(float, input("Digite os três lados do triângulo: ").split())

class Triangulo:
    def __init__(self, lA, lB, lC):
        self.lA = lA
        self.lB = lB
        self.lC = lC

    def calcPerimetro(self):
        p = self.lA + self.lB + self.lC
        print(f"PERÍMETRO: {p}")

    def calcMaiorLado(self):
        lados = [self.lA, self.lB, self.lC]
        print(f"MAIOR LADO: {max(lados)}")

triangulo1 = Triangulo(lA, lB, lC)
triangulo1.calcMaiorLado()
triangulo1.calcPerimetro()