const readline = require('readline-sync')
console.clear()

let n1 = readline.questionInt('Digite um numero : ')

console.clear()

if (n1 % 2 == 0){
    console.log(n1 + ' é um numero par')
} else {
    console.log(n1 + ' é um numero impar')
}