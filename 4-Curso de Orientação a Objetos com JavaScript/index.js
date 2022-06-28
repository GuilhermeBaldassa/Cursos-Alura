import { Cliente } from "./Cliente.js";
import { Gerente } from "./Funcionarios/Gerente.js";
import { Diretor } from "./Funcionarios/Diretor.js";
import { SistemaAutenticacao } from "./SistemaAutenticacao.js";

const diretor = new Diretor("Guilherme", 10000, 123123132);
diretor.cadastrarSenha("123456");
const gerente = new Gerente("Luiz", 5000, 132456621);
gerente.cadastrarSenha("123");

const estaLogado = SistemaAutenticacao.login(diretor, "123456");

console.log(estaLogado);