// cabeçalho para incluir printf, scanf e fgets
// em programas javascript

var scanf_stub = require('scanf-printf-obi').scanf,
    printf_stub = require('scanf-printf-obi').sprintf,
    fgets_stub = require('scanf-printf-obi').fgets

function scanf(format) {
    var res = scanf_stub.apply(this, Array.prototype.slice.call(arguments, 0));
    eval(res);
}

function printf(args){
    var res = printf_stub.apply(this, Array.prototype.slice.call(arguments, 0));
    process.stdout.write(res);
}

function fgets(args){
    var res = fgets_stub.apply(this, Array.prototype.slice.call(arguments, 0));
    eval(res);
}
// final de cabeçalho

  
// exemplo de solução
  
// declara duas variáveis
var val1, val2;

// lê dois valores inteiros
scanf("%d%d", "val1", "val2");

// escreve o resultado
if (val1 > val2)
    printf("%d\n", val1);
else
    printf("%d\n", val2);