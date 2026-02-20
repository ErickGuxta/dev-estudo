class funcionario :
    def __init__(self, nome, salario) -> None :
        self.nome = nome
        self.__salario = salario
    
    def aumentarSalario(self, porcent):
        porcent = porcent/100

        #aumentar salario

        self.__salario = self.__salario * (1 + porcent)
        print(f"Salário aumentado em {porcent*100:.0f}%")

    def mostrarSaldo(self):
        print(f"SALÁRIO ATUAL: R${self.__salario:.2f} reais"  )

harry = funcionario("Harry", 1000)
harry.aumentarSalario(10)
harry.mostrarSaldo()

