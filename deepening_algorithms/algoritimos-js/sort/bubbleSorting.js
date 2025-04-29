const arr = [3,2,1,4,6,5,7,9,8,10]

const bubbleSort = arr => {

    let n = arr.length
    for (let i = 0; i < n - 1; i++){
        for (let j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1] ) {
                let temporario = arr[j];

                arr[j] = arr[j + 1];
                arr[j + 1] = temporario;
            }
        }
    }
    return arr;

}


console.log(bubbleSort(arr)); // [1,2,3,4,5,6,7,8,9,10]