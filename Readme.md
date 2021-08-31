# Projeto Webapi com 3 micros serviços

Regras de Negocio

###### Sistema permite usuário inserir  mensagem e permitir que outros usuários também deem likes de forma anônima.

###### Sistema gera uma lista de todos os usuários

###### Sistema traz todas as mensagens

# 🚀 Começando para instalação local

\* Uma opção e clonar o projeto do github -->($git clone)[GitHub](https://github.com/rafaellima1412/teste_desenvolvimento.git)

######  crie seu ambiente virtual com : 

```python
python -m venv venv
```

######  Depois de ativado instale as dependências 

```python
pip install -r requirements.txt  
```

###### E por fim execute  o servidor

```python
python manage.py runserver
```

# ⚙️ Executando os testes na aplicação.

###### Nesse projeto para rodar todos os testes.

```python
 py manage.py test 
```

# ⚒️ End Points

## /doc

* Essa rota apresenta todas as opções via Swagger do  menu do sistema.

## /me/mine

* Essa rota e uma sugestão de melhoria caso usuário esteja logado mostre apenas suas mensagens:


## /actions

* Aqui o usuário pode dar like e unlike na mensagem escolhida:

## /user

* Essa rota e listado todos usuários:

## /message

* Essa rota e listado as mensagens, usuário, usuário de destino e todos os likes que a mensagem recebeu:





