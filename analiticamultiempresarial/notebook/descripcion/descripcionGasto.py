#Rutina para consumir API de gastos con Python

import requests


def consumir_api_gastos():

	#1. Definir la url del API
	url = "http://localhost:8080/api/gastos"

	#2. Establecer el metodo HTTP que quiero consumir (GET/POST/PUT/DELETE)
	respuesta = requests.get(url)

	#3. Esperar la respuesta
	respuesta.raise_for_status()

	#4. Verificar que la respuesta viene en JSON
	datos = respuesta.json()

	#5. Devolver los datos
	return datos