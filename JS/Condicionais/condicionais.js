let hora = 20


//IF, ELSE IF E ELSE
if (hora< 12) {
    console.log("Bom dia")
} else if (hora < 18 ) {
    console.log("Boa tarde")

} else{
    console.log("Boa noite")

}

// SWITCH é útil quando você precisa testar vários casos diferentes para uma mesma variável.

let diaSemana = 2

switch (diaSemana) {
    case 1:
        console.log("Segunda Feira")
        break
    case 2:
        console.log("Terça Feira")
        break
    case 3:
        console.log("Quarta Feira")
        break
    default:
        console.log("Outro dia");
        break;
}

// 📌 **Explicação:**

// - Cada `case` é uma condição que verifica o valor da variável `diaSemana`.
// - O `default` é executado se nenhum dos casos for verdadeiro.
// - O `break` impede que o código continue executando outros casos.

// OPERADOR TERNÁRIO

let idade = 18

let aviso = idade >= 18 ? "Pode entrar!" : "Entrada proibida!";
console.log(aviso)