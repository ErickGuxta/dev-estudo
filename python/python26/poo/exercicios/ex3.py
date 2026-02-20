from rich.traceback import install
install()


class Livro:

    def __init__(self, nome: str, qtd_paginas: int, autor: str, preco: float):
        self.nome = nome
        self.qtdPaginas = qtd_paginas
        self.autor = autor
        self.preco = preco

    def getPreco(self) -> float:
        return self.preco

    def setPreco(self, novo_preco: float) -> None:

        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.preco = novo_preco


# teste
if __name__ == "__main__":

    livro = Livro(
        nome="Grande Sertão veredas",
        qtd_paginas=350,
        autor="João Silva",
        preco=49.90
    )

    print("=== Livro criado ===")
    print(f"Nome: {livro.nome}")
    print(f"Páginas: {livro.qtdPaginas}")
    print(f"Autor: {livro.autor}")
    print(f"Preço: R$ {livro.getPreco():.2f}")

    # setando preco
    livro.setPreco(39.90)

    print(f"\nPreço novo: R$ {livro.getPreco():.2f}")

