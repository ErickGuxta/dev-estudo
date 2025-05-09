// Função da Sequência de Fibonacci COM recursividade
// A sequência de Fibonacci é: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

function fibonacci(num) {
    // Caso base: se o número for 0 ou 1, retorna o próprio número
    if (num <= 1) return num;
    
    // Caso recursivo: soma os dois números anteriores
    return fibonacci(num - 2) + fibonacci(num - 1);
}

// Testando a função com diferentes valores
console.log("Fibonacci de 0:", fibonacci(0));  // 0
console.log("Fibonacci de 1:", fibonacci(1));  // 1
console.log("Fibonacci de 2:", fibonacci(2));  // 1
console.log("Fibonacci de 3:", fibonacci(3));  // 2
console.log("Fibonacci de 4:", fibonacci(4));  // 3
console.log("Fibonacci de 5:", fibonacci(5));  // 5

// Sem recursao