function twoNumberSum(array, targetSum) {
    // ordenação do array usando sort e comparação
    let arrayOrdenado = array.sort((a, b) => a - b);

    let leftLimite = 0;
    let rightLimite = arrayOrdenado.length - 1;

    while (leftLimite < rightLimite) {
        let soma = arrayOrdenado[leftLimite] + arrayOrdenado[rightLimite];
        
        if ((soma) === targetSum) return [arrayOrdenado[leftLimite], arrayOrdenado[rightLimite]];

        // se a soma for menor que o target, o leftLimite é encrementado, se não, o rightLimite é decrementado 
        (soma) < targetSum ? leftLimite++ : rightLimite--; 


    }
    return [];

}

console.log(twoNumberSum([9,1,3,4,5], 6))