#Rutina para simular la fuente de datos que almacena datos de los gastos
#id
#fecha "2026-05-06"
#monto
#descripcion

import random
from datetime import datetime, timedelta


def simular_gastos(numeroGastosASimular):

	descripciones = [
		"arriendo",
		"comida",
		"transporte",
		"salud",
		"servicios",
		"educacion",
		"ocio",
		"mercado",
		"ropa",
		"tecnologia",
	]

	fecha_base = datetime(2026, 1, 1)
	simulaciones_gasto = []

	for _ in range(numeroGastosASimular):
		dias_aleatorios = random.randint(0, 364)
		fecha_simulada = (fecha_base + timedelta(days=dias_aleatorios)).strftime("%Y-%m-%d")

		gasto_simulado = {
			"id": random.randint(1, 500),
			"fecha": fecha_simulada,
			"monto": random.randint(10000, 500000),
			"descripcion": random.choice(descripciones),
		}

		#Inyectar errores controlados para simular datos reales con ruido
		probabilidadError = random.random()
		if probabilidadError < 0.2:
			gasto_simulado["id"] = random.choice([None, "", -1])
		elif probabilidadError < 0.4:
			gasto_simulado["fecha"] = random.choice([None, "", "2026-13-40", "texto"])
		elif probabilidadError < 0.6:
			gasto_simulado["monto"] = random.choice([None, "", -5000, -120000])
		elif probabilidadError < 0.8:
			gasto_simulado["descripcion"] = random.choice([
				None,
				"",
				"11",
				"@@@",
				" " + gasto_simulado["descripcion"].upper() + " ",
			])

		simulaciones_gasto.append(gasto_simulado)

	return simulaciones_gasto
