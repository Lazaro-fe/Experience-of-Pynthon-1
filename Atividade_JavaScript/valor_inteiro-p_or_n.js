const readline = require('readline-sync')
console.clear()



//  if (numero > 0){
//    console.log(numero + 'é positivo')
//} else {
//    console.log(numero + 'é negativo')
//  }

function verificar(){
    if (numero > 0){
        console.log("Positivo")
    }else{
        console.log("Negativo")
    } 
}

console.log()
let numero = readline.questionInt('Digite um numero : ')
verificar(numero)