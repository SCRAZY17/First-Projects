//si queremos saltarnos una operacion en concreto puedes utilizar la operacion CONTINUE---->

let x = 1;
let y = 1;
let i = x+y;

while (i < 144) {
    i++;
    if (i === 5) {
        continue;
    }
    if (i === 12) {
        break;
    }
    console.log(i);
}