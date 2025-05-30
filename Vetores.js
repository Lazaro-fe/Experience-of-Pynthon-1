//  CRIANDO UM VETOR
const alunos = ['Marta', 'José', 'Maria']
console.log('\n== EXIBINDO TODOS OS ELEMENTOS ==')
console.log(alunos)

console.log('\n== EXIBINDO APENAS O PRIMEIRO ELEMENTO ==')
console.log(alunos[0])

console.log('\n== EXIBINDO APENAS O ÚLTIMO ELEMENTO ==')
console.log(alunos[2])

console.log('\n== ADICIONANDO UM ELEMENTO NO FINAL DO VETOR ==')
alunos.push('ANA')
console.log(alunos)

console.log('\n== REMOVENDO UM ELEMENTO NO FINAL DO VETOR ==')
alunos.pop()
console.log(alunos)

console.log('\n== REMOVENDO APENAS UM ELEMENTO DO VETOR ==')
alunos.pop(2) //    REMOVENDO O TERCEIRO ELEMENTOS DO VETOR
console.log(alunos)