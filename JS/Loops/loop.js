// for
let lista = ['moto', 'carro', 'bicicleta']

for (let i = 0; i < lista.length; i++){
    console.log(lista[i])
}

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