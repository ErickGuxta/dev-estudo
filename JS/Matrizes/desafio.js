// Crie um tabuleiro de xadrez 8x8, preenchendo-o com "⬜" e "⬛".


let colunas = 8
let linhas = 8
let matriz = []


//os quadrados brancos vão ficar em posições ímpares e os pretos em posições pares

for(let i = 0; i < colunas; i++ ){
    matriz[i] = []
    for(let j = 0; j < linhas; j++){
        if ((i + j) % 2 === 0) {
            matriz[i][j] = '⬜'
        } else{
            matriz[i][j] = '⬛'
        }
    }

}

// PARA MOSTRAR O TABULEIRO:

for(let i = 0; i < matriz.length; i++){
    console.log(matriz[i].join(''))
}


        //OBS: O método .join() é usado em arrays no JavaScript para unir todos os elementos de um array em uma única string, separando-os com um delimitador especificado