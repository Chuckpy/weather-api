# Weather-APP

- [Weather-APP](#weather-app)
  - [Setup](#setup)
  - [API's REST :](#apis-rest)

## Setup

Comece clonando o repositório:

```sh
$ git clone https://github.com/Chuckpy/weather-api.git  
$ cd weather-api
```

## Usando o Docker

Basta criar os containers :

```sh
$ docker-compose up --build
```

Adicionar sua chave da api, nas variaveis de ambiente  (.env.example). Caso você ainda não tenha uma, basta se cadastrar no site [oficial da aplicação](openweathermap.org) e ter acesso a sua chave privada

Feito isso, basta substituir o valor "API_KEY" no arquivo ".env.env" para sua chave e retirar o ".example" do arquivo de ambiente principal

E ... pronto !

Podemos testar as rotas do app principal :

```sh
$ docker exec fast_api_web pytest
```

Caso não haja nenhum erro, o servidor estará disponível localmente em `http://127.0.0.1:8000/`.

## API's REST :

Você pode encontrar a documentação de cada app navegando por aqui.

- [Weather](docs/weather.md)
  