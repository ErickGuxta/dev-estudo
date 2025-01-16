let matriz = [
    [2, 3, 4], //linha 0
    [3, 9, 10], //linha 1
    [8, 20, 10] //linha 2
];


//COMO INTERAR (PERCORRER) UMA MATRIZ:

for (let i = 0; i < matriz.length; i++) {
    let element = matriz[i];
    for(let j = 0; j < element.length; j++){
        console.log(matriz[i][j])
    }
}

//SOMAR TODOS OS VALORES DE UMA MATRIZ
let soma = 0
for(let i = 0; i < matriz.length; i++){
    for(let j = 0; j < matriz[i].length; j++){
        soma += matriz[i][j]
    }

}

//ENCONTRAR O MAIOR VALOR DE UMA MATRIZ
let maior = matriz[0][0]
for(let i = 0; i < matriz.length; i++){
    for(let j = 0; j < matriz[i].length; j++){
        if (matriz[i][j] > maior) {
            maior = matriz[i][j]
        }
    }

}

//SOMA DOS ÍNDICES DE UMA MATRIZ
let linhas = 3
let colunas = 3
let Matriz = []

for (let i = 0; i < linhas; i++) {
    Matriz[i] = []
    for(let j = 0; j < colunas; j++){
        Matriz[i][j] = i + j
    }
}

console.log(Matriz)