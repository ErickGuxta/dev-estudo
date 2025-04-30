// Pilha de chamada
function saudar(nome) {
    console.log(`Olá, ${nome} !`);
    saudar2(nome);
    console.log(`Preparando para dizer tchau...`);
    tchau();
}

function saudar2(nome) {
    console.log(`Como vai , ${nome} ?`);
}
function tchau() {
    console.log("ok, tchau")
}

saudar("Erick")
