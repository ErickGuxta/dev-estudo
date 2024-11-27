//Variáveis:

let X = null; // tipo number
let nome_variavel = "erick"; // strings
var a = 80; //variaveis
const valor = true; //booleans

var b; //undefined (nã está definido o valor)
console.log(X, nome_variavel, a, valor, b)


//ESCOPO

    // OBS. O var funciona para todo o escopo

    var x = 10; //aqui x é 10

    {
        var x = 2; //aqui x é 2
    }
    
    //aqui x é 2
    console.log(x);

    //OBS. let -> torna a variável única 

    let y = 20; //aqui y é 20

    {
        let y = 10;//aqui y é 10
        console.log(y);
    }

    //aqui y é 20
    console.log(y);


    //OBS. o const não munda por NADA

     
/*
Quando usar var, let ou const?
    1. Sempre declare variáveis

    2. Sempre use se o valor não deve ser alterado -> const

    3. Sempre use se o tipo não deve ser alterado (Arrays e Objetos) -> const

    4. Use apenas se não puder usar let const

    5. Use apenas se você PRECISAR oferecer suporte a navegadores antigos.var 

*/