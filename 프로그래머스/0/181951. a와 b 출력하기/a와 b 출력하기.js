const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    const [a, b] = line.split(' ');
    console.log('a =', a);
    console.log('b =', b);
});

// let input = [];

// rl.on('line', function (line) {
//     input = line.split(' ');
// }).on('close', function () {
//     console.log(`a = ${Number(input[0])}\nb = ${Number(input[1])}`);
// });