# Utilizar o main.py por padrão ao trabalhar com FastAPI.
# Criando um endpoint /api/hello para exibir o recurso Hello World.
# Bibliotecas utilizadas: FastAPI, uvicorn, Query

from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação
    '''
    return {"Hello": "World"}

# gerando um endpoint para listar restaurantes utilizando a biblioteca Query
@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para exibir cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

# resposta [200] significa que requisição foi atendida com sucesso.

# verificando se a requisição foi atendida e imprimindo os dados JSON
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
            
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante':restaurante,'Cardápio':dados_restaurante}
    else:
        print(f'Erro: {response.status_code} - {response.text}')