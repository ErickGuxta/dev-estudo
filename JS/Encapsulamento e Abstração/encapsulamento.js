//Identificadores privados não são permitidos fora dos corpos de classe


class Cofre {
  #senha; // Atributo privado

  constructor(senhaInicial) {
    this.#senha = senhaInicial;
  }

  alterarSenha(novaSenha) {
    this.#senha = novaSenha;
  }

  verificarSenha(senha) {
    return this.#senha === senha;
  }
}

const meuCofre = new Cofre("1234");
console.log(meuCofre.verificarSenha("1234")); // Saída: true
meuCofre.alterarSenha("5678");
console.log(meuCofre.verificarSenha("1234")); // Saída: false

class Conta {
  #saldo;

  constructor(saldoInicial) {
    this.#saldo = saldoInicial;
  }

  depositar(valor) {
    this.#saldo += valor;
  }

  consultarSaldo() {
    return this.#saldo;
  }
}

const minhaConta = new Conta(317.0);
minhaConta.depositar(100);
console.log(minhaConta.consultarSaldo());


//  gerenciador de tarefas

class GerenciadorDeTarefas {
    #tarefas

    constructor() {
        this.#tarefas = []
    }


    adicionarTarefas(tarefa){
        return this.#tarefas.push(tarefa)
    }

    listarTarefas(){
        this.#tarefas.forEach((tarefa, index) => {
            console.log(`${index + 1}. ${tarefa}`);
        })
    }
}

const tasks = new GerenciadorDeTarefas()

tasks.adicionarTarefas("Comprar pão")
tasks.adicionarTarefas("Comprar arroz")
tasks.adicionarTarefas("Comprar feijão")
tasks.listarTarefas()


//Desafio

class User {
  #senha
  constructor(senhaInicial) {
    this.#senha = senhaInicial
  }

  alterarSenha(senhaAtual, novaSenha){
    if (senhaAtual === this.#senha) {
      this.#senha = novaSenha
      console.log('Senha alterado com sucesso!')


    }else {
      console.log('Senha incorreta!')
   }
  }

}

const user1 = new User(1234)
user1.alterarSenha(1234, 12345)

