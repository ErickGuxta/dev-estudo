
const grafo = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy':[],
    'thom':[],
    'jonny': []
}
const vendedor = 'anuj'

//BUSCA EM PROFUNDIDADE COM RECURSÃO:
function buscaEmProfundidade(grafo, pessoa, visitados = new Set()) {
    if (visitados.has(pessoa)){
        return
    } else{
        if (pessoa === vendedor) {
            console.log(`${pessoa} é o vendedor`)
        return;
        } else{
            visitados.add(pessoa)
            grafo[pessoa].forEach(visinho => buscaEmProfundidade(grafo, visinho, visitados));
        }
    }
}

buscaEmProfundidade(grafo, 'you')


//BUSCA EM LARGURA
function buscaEmLargura(grafo, inicio) {
    const fila = [inicio]
    const visitados = new Set()

    while(fila.length > 0){
        const pessoa = fila.shift()

        if(!visitados.has(pessoa)){
            if (pessoa === vendedor) {
                console.log(`${pessoa} é o vendedor`)
                return;
            } else {
                visitados.add(pessoa)
                fila.push(...grafo[pessoa])
            }
        }
    }
}



buscaEmLargura(grafo, 'you')