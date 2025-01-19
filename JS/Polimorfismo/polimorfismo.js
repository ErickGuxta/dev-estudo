class Forma {
    calcularArea() {
      console.log("Área da forma genérica.");
    }
  }
  
  class Quadrado extends Forma {
    constructor(lado) {
      super();
      this.lado = lado;
    }
  
    calcularArea() {
      console.log(`Área do quadrado: ${this.lado * this.lado}`);
    }
  }
  
  class Circulo extends Forma {
    constructor(raio) {
      super();
      this.raio = raio;
    }
  
    calcularArea() {
      console.log(`Área do círculo: ${Math.PI * this.raio ** 2}`);
    }
  }
  
  const formas = [new Quadrado(4), new Circulo(3)];
  
  formas.forEach(forma => forma.calcularArea());
  // Saída:
  // Área do quadrado: 16
  // Área do círculo: 28.274333882308138