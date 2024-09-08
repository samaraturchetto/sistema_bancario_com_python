# Sistema bancário com Python

## 🎯 Objetivo

O sistema foi desenvolvido para um banco que busca monetizar suas operações e desejava implementar três operações essenciais:

- Depósito;
- Saque e;
- Extrato.

Além disso, o cliente pode realizar até três saques diários, com um limite de R$500,00 por saque.

## 🔨 Skills

- `Python`:
  - Variáveis e constantes;
  - Operadores;
  - Laços de repetição;
  - Estruturas condicionais;

## 📝 Como Funciona

O programa iniciará exibindo um menu com as opções:

- Depositar
- Sacar
- Extrato
- Sair

### ⚙️ Operações

#### Depósito:

- Verifica se o valor é positivo;
- Adiciona o valor ao saldo;
- Registra no extrato;

#### Saque:

- Verifica se o valor solicitado é maior que o saldo, se excede o limite de R$500,00 ou se o número de saques diários já foi atingido;
- Reduz o saldo;
- registra o saque no extrato;

#### Extrato:

- Exibe todas as transões registradas até o momento;
- Exite o saldo atual;

#### Sair:

- Encerra o programa

#### ⚠️ Restrições:

- Depósitos negativos;
- Saques negativos;
- Saques superiores ao saldo;
- Saques superiores ao limite de saque diário;
- Respeita o limite de saques diários;

## 📚 Instruções para teste

1. Escolha ou crie um diretório no seu computador;
2. Abra o diretório criado em um editor de código, (ex: [Visual Studio Code](https://code.visualstudio.com/));
3. Inicie o terminal;
4. Clone o repositório usando o comando: $ **git clone https://github.com/samaraturchetto/sistema_bancario_com_python.git**;
5. Navegue até o diretório correto com o comando: $ **cd sistema_bancario_com_python.git**;
6. Com o [Python](https://www.python.org/) já instalado e configurado, digite no terminal: $ **python sistema_bancario_com_python.py** (ou clique no botão "Run Python File" 😁).
