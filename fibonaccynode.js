const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function Fibonacci(n) {
    if (n === 1 || n === 0) {
        return n;
    } else {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}

rl.question('Digite un numero: ', (input) => {
    const n = Number.parseInt(input);
    console.log('La serie es:');

    for (let i = 0; i < n; i++) {
        console.log(Fibonacci(i));
    }

    rl.close();
});

