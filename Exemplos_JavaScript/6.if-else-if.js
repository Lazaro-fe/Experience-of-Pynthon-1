// INSTALAR : npm install readline-sync

const readline = require('readline-sync')

const idade = readline.questionInt('Digite sua idade : ')

if (idade >= 18) {
    console.log('Maior de Idade!')
} else if (idade > 14) {
    console.log('Adolescente!')
} else {
    console.log("Criança!")
}