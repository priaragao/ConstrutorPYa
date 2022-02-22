#1 - Imports
import json

import pytest
import csv
import requests
from requests import HTTPError

'''
CRUD
Aplicacoes      APIs
Create          Post
Research        Get
Update          Put
Delete          Delete

'''

teste_dados_novos_usuarios = [
    (1,'Juca','Pirama','juca@pirama.com'), #user1
    (2,'Agatha','Souza','agatha@sousa.com') #user2
]

teste_dados_usuarios_atuais = [
    (1,'George','Bluth','george.bluth@reqres.in'), #user1
    (2,'Janet','Weaver','janet.weaver@reqres.in') #user2
]
@pytest.mark.parametrize('id,nome,sobrenome,email',teste_dados_usuarios_atuais)
def testar_dados_usuario(id, nome, sobrenome, email): #funcao que testa algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        #print(f'id: {id_obtido}, nome: {nome_obtido}, sobrenome: {sobrenome_obtido}, email: {email_obtido}')
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
    except HTTPError as http_err:
        print(f'Um erro de HTTP aconteceu: {http_err}') #ISTQB, descobriu rodando é falha.
    except Exception as fail: #qualquer excecao sera tratada a seguir
        print(f'Falha inesperada: {fail}')



#funcao que faz algo >> fora do meu computador (teste de integracao)
#API que vamos usar para fazer o teste
#https://reqres.in/api/users/{id}

#leitor do arquivo CSV
def ler_dados_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuarios.csv'
    try:
        with open(nome_arquivo,newline='') as csvfile:
            dados = csv.reader(csvfile,delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv

    except FileNotFoundError:
        print(f'Arquivo nao encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista:{fail}')

@pytest.mark.parametrize('id,nome,sobrenome,email',ler_dados_csv())
def testar_dados_usuarios(id, nome, sobrenome, email): #funcao que testa algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        #print(f'id: {id_obtido}, nome: {nome_obtido}, sobrenome: {sobrenome_obtido}, email: {email_obtido}')
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
    except HTTPError as http_err:
        print(f'Um erro de HTTP aconteceu: {http_err}') #ISTQB, descobriu rodando é falha.
    except Exception as fail: #qualquer excecao sera tratada a seguir
        print(f'Falha inesperada: {fail}')
