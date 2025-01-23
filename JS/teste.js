console.log('Inicio')

function rodarDepoisDe2Segundos(callback) {
    setTimeout(()=>{     //passso uma função anonima como parametro: () => {callback()}
        callback()
    }, 2000)
}

rodarDepoisDe2Segundos(() => {
    console.log('Rodando depois de 2 segundos')
})



//sem função anonima
function executarCallback() {
    console.log("Rodando depois de 2 segundos")
}

function rodarDepoisDe2Segundos(callback) {
    setTimeout(callback, 2000) // Passa a função nomeada como callback
}

rodarDepoisDe2Segundos(executarCallback)


console.log('Fim')
