const lista_de_numeros = [1, 2, 3, 4, 5, 6]

console.log('=== Listando todos os numeros ====')
console.log(lista_de_numeros)

console.log('\n=== Filtrando elementos pares ===')
const pares = lista_de_numeros.filter(numeros => numeros % 2 === 0)
console.log(pares)

console.log('\n=== Filtrando elementos Impares ===')
const impares = lista_de_numeros.filter(numeros => numeros % 2 !== 0)
console.log(impares)