# Ferramenta em Python que permite modificar ou estender o comportamento de 
# funções e classes de forma limpa e reutilizável.

# A sintaxe @ é um açúcar sintático para aplicar decoradores


print("\n ----DECORADORES----")


def meu_decorador(func):
    # Esta função interna é o "wrapper" (envoltório)
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

# ----- Quando usamos @meu_decorador, é o mesmo que: -----
# resultado_funcao = meu_decorador(minha_funcao)
# print(resultado_funcao()) 

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) :
        print("Antes da função ser chamada(decorador de classe)")
        self.func()
        print("Depois da função ser chamada(decorador de classe)")
        
@MeuDecoradorDeClasse
def segunda_funcao():
    print("Minha segunda função foi chamada")

segunda_funcao()