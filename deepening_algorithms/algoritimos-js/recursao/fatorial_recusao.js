
// Função fatorial sem recursividade

function fatorial(x) {
    let result = 1;
    for (let i = x; i > 0; i--) {
        result *=  i;
    }
    return result;
}

console.log(fatorial(5)); 

// Função fatorial COM recursividade

function fat_recursao(x) {
    if (x == 1 || x == 0 )return 1;
    else return x * fat_recursao(x -1);
}

console.log(fat_recursao(5))

