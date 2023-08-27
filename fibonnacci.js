
var n;

function Fibonacci(n) {
    if (n === 1 || n === 0) {
        return n;
    } else {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}

n = Number.parseInt(prompt('Digite un numero'));
console.log('La serie es:');

for (var i = 0; i < n; i++) {
    console.log(Fibonacci(i));
}

