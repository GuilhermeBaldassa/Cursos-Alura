console.log(`Trabalhando com listas`);
// const salvador = `Salvador`;
// const saoPaulo = `São Paulo`;
// const rioDeJaneiro = `Rio de janeiro`;

const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

listaDeDestinos.push(`Curitiba`); //adicionando um item na lista;

console.log(listaDeDestinos);

const lista = [`Laranja`, `Limão`, `Maça`];
console.log(lista);
console.log(lista[1]); //imprime o conteúdo do index

listaDeDestinos.splice(1,1); //splice deleta o elemento indicado no index.
console.log(listaDeDestinos);

console.log(listaDeDestinos[1]);//imprimir o valor do index;