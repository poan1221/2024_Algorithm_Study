const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    const [a, b] = line.split(' ');
    console.log(`${a} + ${b} = ${parseInt(a) + parseInt(b)}`)
})