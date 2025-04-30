
// Função fatorial sem recursividade

function fatorial(x) {
    let fat = 1;
    for (let i = x; i > 0; i--) {
        fat = fat *  i;
    }
    return fat;
}

console.log(fatorial(5)); 

// Função fatorial COM recursividade

function fat_recursao(x) {
    if (x == 1 )return 1
    else return x * fat_recursao(x -1)
}

console.log(fat_recursao(5))

