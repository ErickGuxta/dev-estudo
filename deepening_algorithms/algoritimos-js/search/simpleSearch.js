// tempo de execução O(n)

const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const search = (num) => {
    for (let i = 0; i < array.length; i++) {
        if (num === array[i]) return i
    }
    return -1;
};

console.log(search(6));
console.log(search(8))

