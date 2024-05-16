// si quieres ejecutar una variable con varios valores tienes que hacer lo siguiente--->

let MisHobbies = ['chess','draw','ride'];

for (let todo of MisHobbies) { 
console.log(todo);
}/* esto crea una variable dentro de la condicion de FOR usando el operador OF
  y asi se puede vincular a la variable anterior en tu funcion*/

let i = 0;
while (i < MisHobbies.length) {
    console.log(MisHobbies[i]);
    i++;
}