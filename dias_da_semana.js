const readline = require('readline-sync')
console.clear()

let dia_da_semana = readline.question('Escolha um dia da semana : ')
console.clear()

if (dia_da_semana == 'Segunda-feira') {
    console.log('Segunda-feira é um dia útil')
} else if (dia_da_semana == 'Terça-feira') {
    console.log('Terça-feira é um dia útil')
} else if (dia_da_semana == 'Quarta-feira') {
    console.log('Quarta-feira é um dia útil')
} else if (dia_da_semana == 'Quinta-feira') {
    console.log('Quinta-feira é um dia útil')
} else if (dia_da_semana == 'Sexta-feira') {
    console.log('Sexta-feira é um dia útil')
} else if (dia_da_semana == 'Sábado') {
    console.log('Sábado é final de semana')
} else if (dia_da_semana == 'Domingo') {
    console.log('Domingo é final de semana')
} else {
    console.log("Inválido!!!")
}
