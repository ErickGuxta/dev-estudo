/*                              ->BEBE
PEÇA TEM UM TIPO E TAMANHO    -> CAMISA   ->INFANTIL
                                ->PEQUENO
                                ->MEDIA
                                ...

                    -> CALÇA    ->BEBE
                                -> INFANTIL
                                ->PEQUENA
                                ->MEDIA
                                ...
      

*/
// var matriz = [Array(m).fill().map(() => Array(n).fill(null))];


var m, n;
scanf ("%d %d", "m", "n");

var matriz = [];

for (var i = 0; i < m; i++) {
    matriz.push(new Array(n), fill(0));
}

console.log(matriz);
