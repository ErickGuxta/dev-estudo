class No {
  constructor(valor) {
    this.valor = valor;
    this.filhos = [];
  }

  adicionarFilho(no) {
    this.filhos.push(no);
  }
}

const raiz = new No("A");
const noB = new No("B");
const noC = new No("C");

raiz.adicionarFilho(noB);
raiz.adicionarFilho(noC);

const noD = new No("D");
const noE = new No("E");

noB.adicionarFilho(noD);
noC.adicionarFilho(noE);

//IMPLEMENTANDO ALGORIMO BUSCA EM PROFUNDIDDADE

function buscaEmProfundidade(no) {
  console.log(no.valor);
  no.filhos.forEach((filho) => buscaEmProfundidade(filho));
}

buscaEmProfundidade(raiz)

//IMPLEMENTANDO ALGORIMO BUSCA EM LARGURA

function buscaEmLargura(){
    const fila = [raiz]
    while (fila.length > 0) {
        const no = fila.shift() //Removes the first element from an array and returns it
        console.log(no.valor)
        no.filhos.forEach(filho => fila.push(filho)) // adicionando os filhos na lista, para repetir o laço
    }
}

buscaEmLargura(raiz)