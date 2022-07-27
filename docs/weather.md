# Weather-APP

O app principal é o weather app, por aqui você pode acessar os dados de clima a partir do id da cidade, e listar suas pesquisas

- [Weather-APP](#weather-app)
  - [List](#list)
  - [Get By id](#get-by-id)
  - [Create](#create)


## List

Essa API retorna todas as buscas feitas, caso alguma tenha sido armazenada no banco

```
GET /weather/
```

response

```json
[
	{
		"id": 1,
		"humidity": 86.0,
		"created": "2022-07-26T23:58:39.588308",
		"city_id": 3439525,
		"temperature": 20.45
	},
    . . . 
]
```

## Get By ID

Essa API retorna uma busca pelo elemento com o ID passado como parâmetro da url

```
GET /weather/<ID>
```

response

```json
{
	"id": <ID>,
	"temperature": 20.9,
	"created": "2022-07-27T00:25:09.709085",
	"city_id": 3439525,
	"humidity": 84.0
}
```

## Create

Por essa API você pode fazer buscas de dados climáticos pelo id da cidade e injetar a resposta no banco de dados

```
POST /weather/
```

Por ser um POST, um Payload é necessário :

```json
{
	"city_id" : "3439525"
}
```

response

```json
{
    "id": 1,
    "humidity": 86.0,
    "created": "2022-07-26T23:58:39.588308",
    "city_id": 3439525,
    "temperature": 20.45
}
```




