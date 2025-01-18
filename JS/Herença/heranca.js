class Veiculo {
    constructor(marca, modelo) {
        this.marca = marca
        this.modelo = modelo        
    }

    imprimirInformações(){
        console.log(`${this.marca} - ${this.modelo} `)
    }
}

class Carro extends Veiculo {   //OBS: extends serva para sinalizar que carro está herdando propriedade e métodos de veiculo
    constructor(marca, modelo, numeroPortas){
        super(marca, modelo)  //chamdo para o construtor da classe pai
        this.numeroPortas = numeroPortas
    }
    abrirPorta(){
        console.log(`${this.marca} ${this.modelo} possui ${this.numeroPortas} portas`)
    }
}

const carro1 = new Carro('Toyota' , 'Hillux', '4');
carro1.imprimirInformações()
carro1.abrirPorta()
