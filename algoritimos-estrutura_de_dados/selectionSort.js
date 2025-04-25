const array = [5, 3, 6, 2, 10];

const menorIndice = (array) => {

    let menorIndice = 0;
    let menorValor = array[0];

    for (let i=0; i < array.length; i++){
        let valor = array[i]
        if (valor < menorValor) {
            menorValor = valor;
            menorIndice = i;
        } 
    }
    return menorIndice;
}

const selectionSort = (array) => {
    const novoArray = [];

    while (array.length > 0) {
        const indexMenor = menorIndice(array);
        const menorNumero = array.splice(indexMenor, 1)[0];
        novoArray.push(menorNumero);
    }

    return novoArray;
}

console.log(selectionSort(array));