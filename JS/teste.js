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
meuCarro.acelerar