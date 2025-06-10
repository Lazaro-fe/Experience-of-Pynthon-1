const lista_de_numeros = [12, 45, -67, 56, -34, -58]
let positivos = 0
let negativos = 0
const soma = 0
console.clear()

console.log('=== Filtrando Números ===')
lista_de_numeros.forEach(lista_de_numeros =>{
    if(lista_de_numeros < 0){
        negativos += 1;

    } else if (lista_de_numeros > 0){
        soma += lista_de_numeros;

    }
})

console.log('A quantidade de negativo è de : ', negativos)
console.log('A quantidade de positivos é de : ', soma)