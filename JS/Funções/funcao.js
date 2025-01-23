function calcular(a, b, operacao) {
  switch (operacao) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      return a / b;
    default:
      return "Operação inválida";
  }
}

console.log(calcular(10, 5, "+")); // Saída: 15
