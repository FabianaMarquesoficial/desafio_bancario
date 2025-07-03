# desafio_bancario
Desafio Bancario
Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python, com funcionalidades para gerenciamento de clientes, contas bancárias, depósitos, saques, extrato e aplicação de rendimento para contas poupança.

Funcionalidades

Cadastro de novos clientes

Abertura de contas (Corrente ou Poupança)

Listagem de contas

Realização de depósitos

Realização de saques

Emissão de extrato bancário

Aplicação de rendimento para contas poupança

Exibição da quantidade total de clientes

Como Executar

Certifique-se de ter o Python 3 instalado.

Salve o código em um arquivo chamado sistema_bancario.py.

No terminal ou prompt de comando, navegue até o diretório do arquivo e execute:

python sistema_bancario.py

Menu do Sistema

=== MENU ===
[1] Novo Cliente
[2] Nova Conta
[3] Listar Contas
[4] Depositar
[5] Sacar
[6] Extrato
[7] Aplicar Rendimento
[8] Total de Clientes
[0] Sair

Detalhes do Sistema

Cliente: Armazena informações do cliente como nome, data de nascimento, CPF, endereço e contas.

ContaCorrente: Conta com limite de saque e número máximo de saques.

ContaPoupanca: Conta que permite aplicação de rendimento mensal.

Historico: Armazena todas as transações realizadas.

Transacoes: Representadas pelas classes Saque e Deposito.

Observações

O CPF deve ter exatamente 11 dígitos.

As contas podem ser de dois tipos: Corrente ou Poupança.

A aplicação de rendimento só é permitida após 30 dias desde o último rendimento.

Autor

Este sistema foi desenvolvido por Fabiana Marques como parte dos estudos na área de programação em Python e gestão bancária.
