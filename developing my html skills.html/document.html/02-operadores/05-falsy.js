// short-circuit o corto circuito

/** los valores que equivalen a false cuando los evaluas:
 * false
 * null
 * ''
 * 0
 * undefined
 * NaN
y estos valores son los que llamamos FALSY.*/ 
// todos los demas valores equivalen a true

let nombre = '';
let NombreDeUsuario = 'Anonimous';
console.log(nombre || NombreDeUsuario);

let nombre2 = 'SCRAZY';
let NombreDeUsuario2 = 'Anonimous';
console.log(nombre2 || NombreDeUsuario2);


function fn1() {
    console.log('Hello');
    return 0;
}

function fn2() {
    console.log('World');
    return true;
}

const x = fn1() && fn2();
