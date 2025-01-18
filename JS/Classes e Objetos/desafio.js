//Implemente uma classe ContaBancaria com os métodos depositar e sacar.

class ContaBancaria {
    constructor(saldoInicial = 0) {
        this.saldo = saldoInicial
    }

    depositar(valor){
        
        this.saldo += valor

        console.log(`Você depositou ${valor}. Seu saldo é ${this.saldo}`)
        
    }

    sacar(valor){
        this.saldo -= valor

        console.log(`Você sacou ${valor}. Seu saldo é ${this.saldo}`)

    }
}

const cb = new ContaBancaria()

cb.depositar(20)
cb.sacar(100)


// Crie uma classe Agenda para armazenar e exibir contatos.

class Agenda {
    constructor() {
        this.contatos = []
    }

    adicionarContato(nome, numero){
        return this.contatos.push(`${nome} : ${numero}`)
    }

    removerContato(nome){
        const indice = this.contatos.findIndex(contato => contato.startsWith(`${nome}:`));
        return this.contatos.splice(indice, 1)

    }

    exibirContatos(){
        console.log(this.contatos)
    }
}

const agenda1 = new Agenda()
agenda1.adicionarContato('Erick', 77998094236)
agenda1.adicionarContato('Gustavo', 77998094236)
agenda1.adicionarContato('Cinthia', 77998094236)

agenda1.removerContato('Cinthia')

agenda1.exibirContatos()
