Para executar o Ambiente Virtual, são necessários dois comandos:

1. Instalação: python -m venv venv (onde o 1o venv é o ambiente virtual e o segundo é o nome da pasta)
2. Executar: venv\Scripts\activate.bat
3. Sair: deactivate

Observação: não funciona no PowerShell, apenas no CMD.

Sobre instalações:

O comando 'pip install requirements' instala os requisitos para rodar os arquivos.
O comando 'pip freeze' lista os arquivos instalados.
O comando 'pip freeze > requirements.txt' gera um arquivo txt com os arquivos requisitados pelo projeto.

Tudo instalado pelo pip será instalado na pasta 'Lib'.



!!!! Para saber mais: desenvolvendo APIs com Python !!!!

Como vimos, as APIs desempenham um papel fundamental na interconexão de sistemas e no compartilhamento de dados entre diferentes aplicações, fazendo uma conexão entre usuário e servidor.

Ao escolher um framework para desenvolver uma API, é crucial considerar diversos fatores. Primeiramente, os requisitos específicos do projeto, incluindo complexidade, escalabilidade e desempenho esperado, devem ser cuidadosamente analisados. A facilidade de uso, suporte da comunidade, integração, documentação, desempenho, segurança, suporte a bancos de dados e a visão futura do framework são elementos essenciais a serem ponderados.

Dentre as várias opções disponíveis para o desenvolvimento de APIs em Python, destacam-se Flask, Django e FastAPI, cada uma com suas características distintas.



>>>>>>> Flask: Simplicidade e Flexibilidade
Flask é conhecido por sua simplicidade e facilidade de uso. É uma escolha popular para projetos menores ou para desenvolvedores que preferem ter mais controle sobre os componentes que utilizam. Com Flask, você pode rapidamente criar uma API básica com poucas linhas de código, sendo uma excelente opção para prototipagem rápida, como mostrado no código a seguir:

from flask import Flask

app = Flask(__name__)

@app.route('/api')
def ola_mundo():
    return 'Olá Mundo!'

if __name__ == '__main__':
    app.run()

>>>>>>>> Django: Estrutura Poderosa e Convenções Batteries-Included
O Django é uma escolha robusta para projetos mais complexos e de maior escala.
Ele fornece uma estrutura completa que inclui um sistema de administração, ORM (Object-Relational Mapping) e muitos outros recursos.
Apesar de ser um framework mais pesado em comparação com Flask, o Django oferece uma solução abrangente para desenvolvimento web.
Um exemplo de como criar uma API simples em Django está no código a seguir:

from django.http import JsonResponse
from django.views import View

class MinhaAPI(View):
    def get(self, request):
        return JsonResponse({'message': 'Olá mundo!'})


>>>>>>>> FastAPI: Alta Performance e Documentação Automática
Como vimos, FastAPI é uma escolha moderna, otimizada para alta performance e fácil utilização.
Ele utiliza a tipagem de dados do Python 3.7+ para oferecer uma documentação automática excepcional, facilitando a compreensão e utilização da API.

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def ola_mundo():
    return {"message": "Olá Mundo!"}

Independentemente da escolha entre Flask, Django ou FastAPI, o importante é considerar os requisitos específicos do projeto,
a experiência da equipe de desenvolvimento e as características desejadas na API. Cada framework tem seus pontos fortes,
e a seleção depende das necessidades particulares das pessoas desenvolvedoras e do contexto do projeto.

O que aprendemos?

Instalamos a biblioteca FastAPI e configuramos um ambiente para criar uma API utilizando Python;

Criamos um endpoint utilizando o FastAPI para disponibilizar recursos relacionados aos restaurantes, permitindo que usuários acessem
informações específicas sobre esses estabelecimentos;

Adicionamos um endpoint que pode receber um parâmetro de consulta (query parameter) para filtrar restaurantes com base em seus nomes,
proporcionando uma maneira flexível de buscar informações específicas;

Utilizamos as ferramentas de documentação docs e redoc do FastAPI para gerar automaticamente documentação interativa para a API,
facilitando a compreensão dos endpoints disponíveis e permitindo testes diretos na interface de documentação.