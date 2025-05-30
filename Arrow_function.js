//  FUNÇÃO
const somar = (a, b) => a + b

const subtracao = (a, b) => a - b

const multiplicar = (a, b) => {
    return a * b
}

const dividir = (a, b) => {
    return a / b
}
//  CHAMANDO A FUNÇÃO
const soma = somar(2,3)
const subtrair = subtracao(2,3)
const multi = multiplicar(2,3)
const divisao = dividir(2,3)

//  EXIBINDO RESULTADOS
console.log(`Soma : ${soma}`)
console.log(`Subtração : ${subtrair}`)
console.log(`Multiplicação : ${multi}`)
console.log(`Subtração : ${divisao}`)