function buscaEmProfundidade(grafo, no, visitados = new Set()) {
    if (visitados.has(no)) return;
    console.log(no)
    visitados.add(no)
    grafo[no].forEach(element => buscaEmProfundidade(grafo, element, visitados));

}

const grafo = {
  1: [2, 5],
  2: [1, 4, 3],
  3: [2, 4],
  4: [2, 3, 5, 6],
  5: [1, 4],
  6: [4],
};

buscaEmProfundidade(grafo, 1);
