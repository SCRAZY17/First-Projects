let i = 0;
while (i <= 6) {
    if (i % 2 == 0) {
        console.log('numero par:', i);
    }
    i++;
}

// FOR es literalmente WHILE pero ejecuta todo en una solo linea
/*ejemplo:
for (la variable, la condicion, la operacion o expresion);
*/
// NUNCA TE OLVIDES DE ESCRIBIR i++ O SINO ENTRARAS EN UN LOOP INFINITO!!!

for (let i = 0; i <= 6; i++) {
    if (i % 2 == 0) {
        console.log('numero par:', i);
    }
}