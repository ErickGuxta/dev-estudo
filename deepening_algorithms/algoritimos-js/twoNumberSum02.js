function twoNumberSum(array, targetSum) {
    let resultado = [];

    for (let i = 0; i < array.length; i++) {
        for(let j = i+1; j < array.length; j++){

            if (array[i] + array[j] === targetSum) {
                resultado.push(array[i]);
                resultado.push(array[j]);
                return resultado;
            }
        } 
    }
    return resultado;
}

console.log(twoNumberSum([9,1,3,4,5], 10))