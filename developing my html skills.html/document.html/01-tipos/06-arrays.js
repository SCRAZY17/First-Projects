//  js respeta el orden de los arrays al contrario de los let y const
const servicios = ['Personalized websites', 'virtual menus', 'HTML courses'];

console.log(servicios);
console.log(servicios[0]);
/* 
si quieres agregar elementos al array--->*/
servicios[3] = 'hola mundo';
/*y si te saltas de numeros las casillas que te saltaste saldran vacias 
en el codigo de la consola.
y si intentas seleccionar un array 'empty' te saldra 'undefined'.
los arrays se comportan como object.
*/
console.log(typeof servicios);
/*
    para ver el numero de lineas de tu array debes--->
*/ 
console.log(servicios.length);