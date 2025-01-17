function inverterString(str) {
    if (str === "") return ""; // Caso base
    return inverterString(str.slice(1)) + str[0]; // Chamada recursiva
  }
  
  console.log(inverterString("recursão")); // Saída: "oãsruceR"


  function somaArray(array) {
    if (array.length === 0) return 0; // Caso base
    return array[0] + somaArray(array.slice(1)); // Chamada recursiva
  }
  
  console.log(somaArray([1, 2, 3, 4])); // Saída: 