# Prática de Class e POO

Projeto simples em Python desenvolvido para praticar os conceitos de **Classes** e **Programação Orientada a Objetos (POO)**.

O sistema simula uma plataforma de streaming, onde um cliente possui um plano (`basic` ou `premium`) e pode assistir filmes de acordo com as regras definidas no código.

## Objetivo

Este projeto foi criado com foco em aprendizado, para treinar:

- Criação de classes
- Uso do método `__init__`
- Atributos de instância
- Métodos de classe
- Validação de dados
- Regras de negócio com condicionais

## Funcionalidades

- Cadastro de cliente com:
  - nome
  - email
  - plano
- Validação do plano escolhido
- Alteração de plano
- Verificação de acesso a filmes conforme o tipo de plano
- Mensagem de upgrade para usuários do plano básico

## Estrutura do projeto

Exemplo de organização dos arquivos:

```bash
projeto/
│── cliente.py
│── main.py

## Testes manuais

Atualmente, o projeto foi validado por meio de testes manuais, executando o arquivo principal e verificando o comportamento da classe `Cliente`.

### Exemplo de teste

```python
from cliente import Cliente

cliente = Cliente("Cesar", "cesar@gmail.com", "basic")
print(cliente.nome)
cliente.mudar_plano("premium")

print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")
