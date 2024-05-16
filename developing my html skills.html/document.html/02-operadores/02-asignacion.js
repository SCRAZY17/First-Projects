let a = 25;
a = a % 5; 
let b = 100; 
b = a % b % 5;
a += 80;
b -= 35
b **= 3

console.log(a);
console.log(b);

function calculo () {
return b%a;
}

console.log(calculo());
/*
la asignacion se usa para cambiar el valor de mas que una unidad encima se puede utilizar para 
todas las operaciones previas---> +-*%/'**'
*/