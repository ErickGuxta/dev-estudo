let nome = 'Erick'
let sobrenome = 'Gustavo'
let saudacao = `Olá, ${nome} ${sobrenome}` // Template literal

console.log(saudacao)

// 📌 Dica: Use template literals (crase) quando precisar incluir variáveis ou expressões diretamente no texto

//ACESAR UMA VARIÁVEL

let palavra = 'Programação'

    console.log(palavra[4])
    console.log(palavra[6])

//OBTER O TAMANHO DA STRING

    console.log(palavra.length)

// VERIFICAR SE CONTÉM UM TEXTO ESPECÍFICO- INCLUDES()

let email = 'gustavocostacnn@gmail.com'

    if (email.includes("@gmail.com")) {
        console.log("Email válido!")
    } else{
        console.log("Email inválido!")
    }

// CORTAR UMA PARTE DO TEXTO - SLICE

let mensagem = 'Estou estudando JavaScript!!'
    console.log(mensagem.slice(6 , 20))
    console.log(mensagem.slice(0 , -5))

// SUBSTITUIR PALAVRA

    let novaMensagem= mensagem.replace("JavaScript", "PHP")
    console.log(novaMensagem)

// VERIFICAR COMEÇO E FIM - starsWith e endWith

let site = 'www.exemplo.com'

    console.log(site.startsWith("www"));  // Saída: true
    console.log(site.endsWith(".com.br"));  // Saída: false

