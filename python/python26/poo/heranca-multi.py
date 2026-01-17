print("\n ----HERANÇA MULTIPLA----")


class Dispositivo:
    def __init__(self, nome, marca) -> None:
        self.nome = nome
        self.marca = marca
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return f"{self.nome} ligado"

    def deligar(self):
        self.ligado = False
        return f"{self.nome} desligado"


class Conectavel:
    def __init__(self) -> None:
        self.conectado = False

    def conectar(self):
        self.conectado = True
        return "Conectado à internet."

    def desconectar(self):
        self.conectado = False
        return "Desconectado da internet."

print("\n ----FAZENDO A HERANÇA MULTIPLA----")

class Smartphone(Dispositivo, Conectavel):
    def __init__(self, nome, marca,modelo, sistema_operacional) -> None:
        # O método super() é usado para chamar métodos da classe pai, o que é essencial para 
        #a extensão(acrescentar mais coisa) de comportamentos em subclasses.
        super().__init__(nome, marca)

        # Atribuutos especificos da classe herdada da classe-pai

        self.modelo = modelo
        self.sistema_operacional = sistema_operacional

    def fazer_ligacao(self, numero):
        if self.ligado == False:
            return "ligue o dispositivo"
        else:
            return f"Ligando para {numero}..."




print("\n ----Intanciando a classe com herança múltipla----")
meu_smartphone = Smartphone("Galaxy S21", "Samsung", "S21", "Android")

print(meu_smartphone.ligar())            # Galaxy S21 ligado.
print(meu_smartphone.conectar())         # Conectado à internet.
print(meu_smartphone.fazer_ligacao("123-456-7890"))  # Ligando para 123-456-7890...
