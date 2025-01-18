const aprovados = ['Erick', 'Cinthia', 'Gustavo']

//No método forEach, você pode passar mais parâmetros para a função de callback. O forEach já fornece três argumentos padrão para o callback:

//OBS: Ordem dos parâmetros do forEach: (string, indice e o array)
//EXEMPLO 1
    aprovados.forEach(function(nome, indice, array) {
        console.log(`${indice + 1} ${nome}`)
        console.log(array)
    })

//EXEMPLO 2
    aprovados.forEach((aprovado, indice, array) => {
        console.log(`${indice + 1} ${aprovado}`)
    });
        //OBS. Não precisa passar todos os parâmetros


// Posso criar os parâmetros de forma externa 

const exibirAprovados = nome => console.log(nome)
aprovados.forEach(exibirAprovados)


