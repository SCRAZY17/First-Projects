function about_us() {
    console.log('our_services');
}

about_us();//<----si no escribes esto el console.log no va a funcionar
/* 
las funciones se pueden utilizar para realizar calculos,
por ejemplo la propiedad del numero 6174---->
*/
function calculo(x) {    //ahora x es un parametro
    return x - 1467;           
}
let resultado = calculo(7641);// y aqui es un argumento

/* 
para saltarte crear una 'const' o 'let' puedes imprimir directamente tu 'function'--->
*/
console.log(calculo());

console.log(resultado);


function calculo(x, y, z) {
    return (x%z)**y;
}
let resultados = calculo(6030, 5, 78);// tienes que arrojar el mismo numero de argumentos que de parametros o la funcion sera erronea
console.log(resultados);
console.log(typeof calculo);