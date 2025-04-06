// Script para animação de digitação em texto
document.addEventListener("DOMContentLoaded", function () {
    const h1 = document.querySelector(".container-left h1");
    const textoOriginal = "Olá, Eu sou Erick";
    let i = 0;

    h1.textContent = " ";
    h1.classList.add("typing");

    function digitar() {
        if (i < textoOriginal.length) {
            h1.textContent += textoOriginal.charAt(i);
            i++;
            setTimeout(digitar, 100); 
        } else {
            h1.classList.remove("typing"); 
        }
    }

    digitar();
});



document.addEventListener('DOMContentLoaded', function (){
    const formEl = this.getElementById('form')
    const emailInput = this.getElementById('email')


    formEl.addEventListener('submit', evento=>{
        evento.preventDefault();

        // validação do email
        if (emailInput.value === "" || !isEmailValid(emailInput.value)) {
            alert("Digite um email válido")
            return
        }


        // Transformando dados(objeto) em json 
        const formData = new FormData(formEl);
        const data = Object.fromEntries(formData)

        const jsonData = {
            nome: data['input-text'],
            email: data['input-email'],
            mensage: data['input-mensage']
        };
        const jsonString = JSON.stringify(jsonData)

        // Enviando dados do json para o php processar USANDO FETCH

        fetch('processar_form.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonString 
        }).then(resposta => resposta.json()).then(data => {
            alert(data.mensagem)
        }).catch(error => {
            alert("Erro ao enviar mensagem")
            console.log(error)
        })

    })
})

// Função para validar email usando regex
function isEmailValid(email) {
    const emailRegex = new RegExp(
        /^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$/
    );

    if (emailRegex.test(email)) {
        return true;
    }
    return false;
}