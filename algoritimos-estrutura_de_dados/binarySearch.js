// tempo de execução O(log n)

const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const search = (num) => {
  let comeco = 0;
  let fim = array.length-1;
  let meio = Math.floor((comeco + fim) / 2); // índice do valor do meio

  while (array[meio] !== num && comeco <= fim) {
    if (num < array[meio]) fim = meio - 1;
    else comeco = meio + 1;

    meio = Math.floor((comeco + fim) / 2);
  }

  return array[meio] === num ? meio : false;
};

console.log(search(6));
