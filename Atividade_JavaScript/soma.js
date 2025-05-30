const readline = require('readline-sync')
console.clear()

let A = readline.questionInt('Digite o primeiro numero : ')
let B = readline.questionInt('Digite o segundo numero : ')
let C = readline.questionInt('Digite o terceiro numero : ')
console.clear()
soma = A + B

if (soma > C) {
    console.log('A soma de' ,A, '+' ,B, 'é igual a' ,soma, 'que é maior que' ,C, )
} else {
    console.log('A soma de A + B que resulta em' ,soma, 'é menor que' ,C,)
}

//  OUTRA FORMA DE ESCREVER O CÓDIGO

//   if (soma > C) {
//    console.log('A soma de A + B é maior que C')
//  } else {
//    console.log('A soma de A + B é menor que C')
//  }