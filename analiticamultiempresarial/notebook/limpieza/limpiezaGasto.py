#Limpiamos datos de gastos para garantizar consistencia antes de analizar

import pandas as pd


def limpiar_datos_gasto(data_frame_gasto):

	#1. LIMPIAR TEXTO
	data_frame_gasto["descripcion"] = (
		data_frame_gasto["descripcion"].astype("string").str.strip().str.lower()
	)

	valores_esperados_descripcion = [
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
	data_frame_gasto["descripcion"] = data_frame_gasto["descripcion"].where(
		data_frame_gasto["descripcion"].isin(valores_esperados_descripcion),
		pd.NA,
	)

	#2. LIMPIAR NUMEROS
	data_frame_gasto["id"] = pd.to_numeric(data_frame_gasto["id"], errors="coerce")
	data_frame_gasto["monto"] = pd.to_numeric(data_frame_gasto["monto"], errors="coerce")

	data_frame_gasto = data_frame_gasto[data_frame_gasto["id"] > 0]
	data_frame_gasto = data_frame_gasto[data_frame_gasto["monto"] > 0]

	#3. LIMPIAR FECHAS
	data_frame_gasto["fecha"] = pd.to_datetime(data_frame_gasto["fecha"], errors="coerce")

	#4. ELIMINAR REGISTROS INVALIDOS EN CAMPOS OBLIGATORIOS
	columnas_obligatorias = ["id", "fecha", "monto", "descripcion"]
	data_frame_gasto = data_frame_gasto.dropna(subset=columnas_obligatorias)

	return data_frame_gasto