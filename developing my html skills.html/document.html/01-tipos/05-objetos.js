let numeroDeLista= 1;
let parrafo= "servicios";
let contenido= true;
let alSeleccionar= null;

let documento= {
    parrafo: "servicios",
    contenido: true,
    numeroDeLista: 1,
    alSeleccionar: null,
};
console.log(documento);
console.log(documento.parrafo);
console.log(documento['contenido']);

documento.numeroDeLista = 3;

delete documento.alSeleccionar;