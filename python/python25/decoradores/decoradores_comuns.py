from zipfile import MAX_EXTRACT_VERSION


print("\n ----@classmethod e @staticmethod ----")

# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome 

    # requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"

    # método de classe: não preciso instanciar a classe para ter acesso ao metodo
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor = {cls.valor}"

    # método estático: é um método que não recebe nem um atributo, mas pode fazer uma função especifica
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"


obj = MinhaClasse(nome = "Classe Exemplo")

print("\n ----Acesso ao método com classe instânciada----")
print(obj.metodo_instancia())

print("\n ----Acesso aos métodos com classe SEM estar instânciada----")
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

print("\n ----EXEMPLO MAIS PRÁTICO----")


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca  = marca 
        self.modelo = modelo 
        self.ano    = ano 


    # exemplo de método em que eu recebo uma tupla de valores
    @classmethod
    def criar_carro(cls, configuracoes):
        carros = []
        for c in configuracoes:
            marca, modelo, ano = c.split(",")
            carros.append(cls(marca, modelo, int(ano)))
        return carros



configuracoes = ("Toyota,Corolla,2022", "Toyota,Hilux,2024", "Volks,Golf,2020", "Chevrolet,Chevette,1980")
carros = Carro.criar_carro(configuracoes)

for carro in carros:
    print(f"Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano}")

  