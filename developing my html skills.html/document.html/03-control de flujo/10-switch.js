let saludo = 'hola';

switch (saludo) {
    case 'hola':
        console.log('buenas');
        break; 
    case 'vete de aqui':
        console.log('pegale');
        break;
    default://<----para un valor no reconocido
        console.log('have not heard what he said');
}
// la operacion switch tiene un bug, por eso siempre tienes que agregar la operacion break en el final de cada case para que tu codigo corra correctamente.
// SWITCH solo simplifica la utilizacion de IF y ELSE para que escribas menos codigo.