# Exercício para trabalhar com APIs, utilizando Python e JSON, utilizando parâmetros para filtrar os dados (cardápios dos restaurantes por restaurante).
# UTILIZANDO FastAPI para rotear as requisições em uma URL.

import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print (response)

# resposta [200] significa que requisição foi atendida com sucesso.

# verificando se a requisição foi atendida e imprimindo os dados JSON
if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'Erro: {response.status_code}')

# criando um arquivo json e escrevendo no arquivo com 'w'
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        # criando o arquivo json, com o parametro dados, o nome do arquivo e a indentação
        json.dump(dados, arquivo_restaurante, indent=4)

print(dados_restaurante["McDonald’s"])
# Items que temos: Company, Item, Price, Description