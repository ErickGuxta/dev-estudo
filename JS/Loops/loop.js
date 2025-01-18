// for
    let lista = ['moto', 'carro', 'bicicleta']

    for (let i = 0; i < lista.length; i++){
        console.log(lista[i])
    }

//for of -> intera por todos os itens do array
    for (const element of lista) {
        console.log(element)
    }

//for in -> usado para interar objetos
    const user = {
        name: 'erick',
        age: 33,
        street: 'Rua Dom Bosco'
    }

    for (let key in object) {
        if (Object.prototype.hasOwnProperty.call(object, key)) {
            const element = object[key];
            
        }
    }

//FOREACH
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


//while

let cont = 0

    while (cont < 10) {
        console.log("Olá")
        cont++

    }

// break e continue

for (let i = 1; i <= 10; i++){
    if (i == 5) break

    console.log(i)
}

for (let i = 1; i <= 10; i++){
    if (i == 5) continue  //o valor de indice 5 não aparece

    console.log(i)
}


// do...while

let numero = 20

do{
    console.log('Executando...')
    numero--
} while (numero > 5)