const readline = require('readline-sync')
console.clear()
const idade = readline.questionInt('Digite sua idade : ')

if (idade < 16) {
    console.log('Não podem votar!')
} else if (idade >= 16 && idade == 17) {
    console.log('Voto Opcional!')
} else if (idade > 18) {
    console.log('Voto Obrigatório!')
} else if (idade > 65) {
    console.log('Não são obrigados a votar!')
}