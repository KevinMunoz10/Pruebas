const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function square(n) {
    // Crea un nuevo array con una longitud de 4 y llena cada elemento con el mismo valor: '+'. Esto no es lo que se desea.
    return Array(10)
        // El método fill() no se está utilizando correctamente aquí. Debería estar llenando con cadenas repetidas, no con un solo caracter.
        .fill('+'.repeat(n))
        // Une los elementos del array usando '\n' como separador para formar un solo string.
        .join('\n');
}

rl.question('Digite un numero: ', (input) => {
    const n = Number.parseInt(input);
    console.log('El cuadraro queda de esta manera')
    console.log(square(n))
    rl.close
}); 
