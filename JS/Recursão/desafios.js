// Escreva uma função para verificar se uma palavra é um palíndromo usando recursão.

function VerificarPalavra(palavra) {
    if (palavra.length <= 1) return true;

    if (palavra[0] !== palavra[palavra.length - 1]) return false;

    return VerificarPalavra(palavra.slice(1, -1))
}

console.log(VerificarPalavra("OVO"))

//Crie uma função que some todos os números de um array usando recursão.

function somarArray(array) {
    if (array.length === 0) return 0;

    return (array[0] + somarArray(array.slice(1)));
}

console.log(somarArray([1,2]))

// Crie uma função que liste todos os arquivos de um diretório usando recursão.

function listarArquivos(diretorio) {
    for(let item of diretorio){
        if (Array.isArray(item)) {
            listarArquivos(item)
        }else{
            console.log(item)
        }

    }
    
}

let arquivos = ["index.html", ["css", "style.css"], ["js", "script.js"]];
console.log(listarArquivos(arquivos))


// Escreva uma função recursiva que conte de n até 0.

function contador(n) {
    if(n < 0) return 0;
    console.log(n)
    
    return contador(n - 1)
}

console.log(contador(8))