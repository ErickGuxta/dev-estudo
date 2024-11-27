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



// MÉTODOS DE ARRAY

const numeros = [40, 100, 200, 20, 500, 800];

//Adicionar ou remover itens

    //push
        numeros.push(55);
        console.log(numeros);
    //pop
        numeros.pop();  //-> remove o último elemento
        console.log(numeros);

//Função para encontrar maior ou menor valor

    //para maior numero
    function MaiorNumero(array) {
        return Math.max.apply(null, array);
    }
    //para menor numero
    function MenorNumero(array) {
        return Math.min.apply(null, array);
    }

document.getElementById("maior").innerHTML = "O maior número é: " + MaiorNumero(numeros)
document.getElementById("menor").innerHTML = "O menor número é: " + MenorNumero(numeros)


// fazer uma filtragem 
    
    function filtragem(value, index, array) {
        return value > 20
    }

    const maior20 = numeros.filter(filtragem);

    document.getElementById("valores-maior20").innerHTML = "Os valores maiores que 20 são: " + maior20



//If, else

    //exemplo 1

    var usuario = "Eric";

    if(usuario == "Pedro") {
        console.log("O nome dele é Pedro");
    } else if(usuario == "Matheus") {
        console.log("O nome é Matheus");
    } else if(usuario == "Eric") {
        console.log("O nome é Eric");
    } else {
        console.log("Ele possui outro nome!");
    }


        //exemplo 2 (com formulario)

function verificarTexto() {
    let texto_input = document.getElementById("texto_input").value;

    if (texto_input == "" || texto_input == null) {
        // document.getElementById("teste").innerHTML = "Campo obrigatório"
        let p = document.getElementById("teste");
        p.innerHTML = "O campo não pode ser vazio"
        p.style.color = "red"
    } else{

        let p = document.getElementById("teste");
        p.innerHTML = "Tudo certo!";
        p.style.color =  "green"
    }
}

//Swith

function verificarCor() {
    let cor = document.getElementById("cor").value;

    switch (cor) {
        case "azul":
            //o que acontece
            document.body.style.backgroundColor = "blue"
            break;
        case "vermelho":
            //o que acontece
            document.body.style.backgroundColor = "red"
            break;
        default:
            //o que acontece
            document.getElementById("teste2").innerHTML = "Cor não disponível"
            break;
    }

}


//For, while