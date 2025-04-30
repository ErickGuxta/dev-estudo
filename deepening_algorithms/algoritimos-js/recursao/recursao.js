// FUNÇÃO DE DECREMENTAÇÃO SEM RECURSAO
const decrementar = (n) => {
    for (let i=n; i > 0; i--) console.log(i);
}

decrementar(20)

// FUNÇÃO DE DECREMENTAÇÃO ----COM RECURSÃO----
const decrementar_recursao = (i) =>{
    console.log(i)
    if (i <= 1) return;
    else decrementar_recursao(i - 1);
}

decrementar_recursao(20)




