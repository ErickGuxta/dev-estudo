// TIPOS DE SAIDA

document.getElementById("texto").innerHTML = "escrito com document.getElementById().innerHTML"

// alert("isso é um alerta");

console.log("hello word");

//VARIAVEIS:


let idade = 17; // tipo number
let nome = "erick"; // strings
var a = 80; //variaveis
const valor = true; //booleans
var b; //undefined (nã está definido o valor)

console.log(idade, nome, a, valor, b)


//ARRAY

let igredientes = ["farinha", "leite", "fermento", "açucar"] // array

console.log(igredientes[3])

var array = [5, "Matheus", true, {teste: 1, teste: 2}]; // obj => {}

console.log(array);



//OBJETOS

const personagem ={  //objeto
    nome: "Erick",
    nivel: 10, 
    forca: 800,
    magia: 10000,


    descricao: function () {
        return "Este usuario, " + this.nome + " ,está no nível " + this.nivel
    },
    correr: function () { 
        console.log('Esta correndo') } // -> isso é um método do meu objeto
}


console.log(personagem.nome)
console.log(personagem.forca)
console.log(personagem.descricao());
personagem.correr();


//FUNÇÃO

 // INPUT
 // PROCESSA
 // OUTPUT

    function sum(a, b){
        let resultado = a + b
        return resultado
    }

    let x = sum(15, 5)
    console.log(x)

//FUNÇÃO SETA

    let sum2 = (a, b) => {
        let resultado = a + b
        return resultado
    }

    let y = sum2(15, 55)

    console.log(y)

//CONDICIONAIS

    const size = 10;

    if (size > 100) {
        console.log("grande");
    } else if (size > 20) {
        console.log("medio");
    } else if (size > 4) {
        console.log("pequeno");
    } else {
        console.log("minusculo");
    }

// OPERADORES
    /* 
        == 
        >=
        <=
        >
        <
        && 
        "!"
        ||
    */




