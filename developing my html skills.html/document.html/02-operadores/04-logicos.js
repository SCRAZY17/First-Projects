// AND, OR, NOT

let usuario = true;
let edad = false;
const enlinea = true;
let amigo = false;

// AND in JS is &&
console.log("operador AND:");
console.log(usuario && edad);
console.log(usuario && enlinea); //the console is gonna pring you a true only if both conditions are true.

console.log("...");
// OR in JS is ||, to write a | you must press the 'alt gr' key and the number '6' key.
console.log("operador OR:");
console.log(usuario || edad);
console.log(usuario || enlinea); 
console.log(edad || amigo); // para que OR te devuelva false la unica manera es que todos los elementos que evalue sean false 

console.log("...");
// NOT in JS is ! just before the element we wanna evaluate, it's regardless if you let a space.
console.log("operador NOT:");
console.log(!edad);

