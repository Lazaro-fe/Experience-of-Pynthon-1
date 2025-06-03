const readline = require('readline-sync')
console.clear()

const numero  = readline.questionInt('Digite um número : ')

for (let i = 1; i <= 10; i++)
    console.log('${numero} x ${i} = ${numero x i}');
