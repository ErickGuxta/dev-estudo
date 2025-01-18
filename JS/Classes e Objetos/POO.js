class Carro{ // declarando a classe
    constructor(marca, modelo, cor){
        this.marca = marca //declarando atributos
        this.modelo = modelo
        this.cor = cor
    }

    acelerar(){ //método
        console.log(`${this.marca} está acelerando!`)
    }
}

const meuCarro = new Carro("Honda", "Civic", "Preto")
meuCarro.acelerar()

//Criando uma classe para um produto

class Produto{
    constructor(nome, preco, id){
        this.nome = nome
        this.preco = preco
        this.id = id
    }

    exibirDetalhes(){
        console.log(`${this.nome} custa R$${this.preco}`)
    }

    exibirID(){
        console.log(`O ID do produto ${this.nome} é ${this.id} `)
    }

}
const produto1 = new Produto("Celular", 2000, "48GBI49")
produto1.exibirDetalhes()
produto1.exibirID()


//simulação de um Bando de Dados

class BancoDados {
    constructor() {
        this.dados = []
    }

    adicionar(dado){
        this.dados.push(dado)
        console.log("Dado adicionado")
    }

    listar(){
        console.log(this.dados)
    }

}

const bd = new BancoDados()
bd.adicionar("Erick")
bd.listar()