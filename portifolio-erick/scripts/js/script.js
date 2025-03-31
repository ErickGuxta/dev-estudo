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



