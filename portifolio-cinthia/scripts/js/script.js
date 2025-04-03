document.addEventListener("DOMContentLoaded", function(){
    const h1 = document.querySelector(".container-left h1");
    const textoOriginal = "Olá, Eu sou Cinthia!";
    let i = 0;

    h1.textContent = " ";
    h1.classList.add("typing");

    function digitar() {
        if (i < textoOriginal.length ) {
            h1.textContent += textoOriginal.charAt(i);
            i++;
            setTimeout(digitar, 120);
        } else{
            h1.classList.remove("typing");
        }   
    }
    digitar()
})

document.getElementById("contactForm").addEventListener("submit", async function (element) {
    element.preventDefault();

    const formData = new FormData(element.target);
    const response = await fetch("send-email.php", {
        method: "POST",
        bady: formData
    });

    const statusMsg = document.getElementById("statusMsg");
    if (resposta.ok) {
        statusMsg.textContent = "mensagem enviada com sucesso"
    } else{
        statusMsg.textContent = "erro ao enviar mensagem";
    }    
})