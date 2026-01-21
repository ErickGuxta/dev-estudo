""" 
    @property transforma MÉTODOS EM ATRIBUTOS, permitindo validação, cálculos e 
    encapsulamento sem mudar a interface pública da classe!

    Ele permite que um método seja acessado como atributo, sem a necessidade de chamá-lo como uma função.

"""

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        return self.largura * self.altura

retangulo = Retangulo(5, 3)
area = retangulo.calcular_area()
print(area)

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    @property
    def area(self):
        return self.largura * self.altura

retangulo = Retangulo(5, 3)
print(retangulo.area)  # Saída: 15

# ---- GETTERS E SETTERS ----   
    # O método getter é responsável por RETORNAR o valor da propriedade quando ela é acessada.
    # O método setter, por sua vez, é usado para DEFINIR o valor da propriedade quando ela é modificada.

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self.altura = altura
    
    @property  #o método largura funciona como o getter
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, nova_largura):
        if nova_largura > 0:
            self._largura = nova_largura
        else:
            raise ValueError("A largura deve ser maior que 0.")
    
    @property
    def area(self):
        return self.largura * self.altura

retangulo = Retangulo(5, 3)
print(retangulo.largura)  # Saída: 5

retangulo.largura = 7
print(retangulo.largura)  # Saída: 7

# ---- DELETAR ----   
    #Além de obter e definir o valor de uma propriedade, também podemos excluí-la utilizando o método deleter.

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self.altura = altura
    
    @property
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, nova_largura):
        if nova_largura > 0:
            self._largura = nova_largura
        else:
            raise ValueError("A largura deve ser maior que 0.")
    
    @largura.deleter
    def largura(self):
        del self._largura
    
    @property
    def area(self):
        return self.largura * self.altura

print(retangulo.largura)
