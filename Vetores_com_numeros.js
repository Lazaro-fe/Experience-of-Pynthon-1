//  Criando um Vetor com Números
const lista_de_numeros = [1, 2, 3, 4, 5]

console.log('=== Listando todos os valores da lista: ===')
console.log(lista_de_numeros)

console.log('\n=== Multiplicando valores por 2: ===')
const dobrados = lista_de_numeros.map(numero => numero * 2)
console.log(dobrados)

console.log('\n=== Filtrando elementos pares: ===')
const pares = lista_de_numeros.filter(numero => numero % 2 === 0)
console.log(pares)

console.log('\n=== Somando todos os números: ====')
const soma = lista_de_numeros.reduce((soma, atual) => soma + atual, 0)
console.log(soma)