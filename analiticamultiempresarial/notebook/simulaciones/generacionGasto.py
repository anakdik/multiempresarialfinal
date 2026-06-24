#Rutina para generar multiples fuentes de datos de un set simulado

import pandas as pd


def convertir_lista_gastos_a_fuentes(lista_datos):

	data_frame_datos = pd.DataFrame(lista_datos)

	data_frame_datos.to_json(
		"gastos.json",
		orient="records",
		indent=4,
	)

	data_frame_datos.to_csv(
		"gastos.csv",
		index=False,
	)