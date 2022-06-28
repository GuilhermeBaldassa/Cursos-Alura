console.log(`Trabalhando com condicionais`);

const listaDeDestinos = new Array(`Salvador`, `São Paulo`, `Rio de Janeiro`);

const idadeComprador = 15;
const estaAcompanhada = true;
const temPassagemComprada = true;

console.log(`Destinos Possíveis: `);
console.log(listaDeDestinos);

// if (idadeComprador >= 18) {
//   console.log(`Comprador Maior de idade.`);
//   listaDeDestinos.splice(1, 1);
// } else if (estaAcompanhada) {
//   console.log(`Comprador está acompanhado.`);
//   listaDeDestinos.splice(1, 1);
// } else {
//   console.log(`Comprador não é maior de idade.`);
// }

if (idadeComprador >= 18 || estaAcompanhada) {
  console.log(`Boa Viagem!`);
  listaDeDestinos.splice(1, 1);
} else {
  console.log(`Comprador não é maior de idade.`);
}

console.log("Embarcando..\n");

if(idadeComprador >= 18 && temPassagemComprada){
    console.log(`Boa viagem`);
}else{
    console.log(`Você não pode embarcar.`);
}
