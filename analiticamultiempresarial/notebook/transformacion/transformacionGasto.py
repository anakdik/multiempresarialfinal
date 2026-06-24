#Rutina para TRANSFORMAR el DataFrame limpio de gastos
#
#TRANSFORMAR = a partir de datos YA limpios, obtener informacion util usando:
#   - query()   -> FILTRA filas (se queda solo con las que cumplen una condicion)
#   - groupby() -> AGRUPA filas que comparten un valor y aplica una operacion
#                  a cada grupo (sum = suma, count = conteo, mean = promedio)
#
#RECUERDE: estas funciones reciben SIEMPRE el data frame YA limpio
#(la salida de limpiar_datos_gasto).
#Columnas disponibles del gasto:  id, fecha, monto, descripcion
#
#Mire como quedo resuelto el ejemplo de USUARIOS en transformarUsuario.py
#y resuelva aqui los 5 ejercicios de GASTOS de la misma forma.

import pandas as pd


#EJERCICIO 1: TOTAL GASTADO POR CATEGORIA (descripcion)   ->  SUM
#GRAFICA QUE DEBE HACER EL ESTUDIANTE EN EL MAIN: grafica_barras
#   eje X = descripcion / eje Y = monto_total
#   (compara cuanto se gasto en cada categoria -> barras)
def total_gastado_por_descripcion(data_frame_gasto):
    #TAREA 1.1 query: quedarse solo con los gastos cuyo monto sea mayor a 0
    #TAREA 1.2 groupby: agrupar por "descripcion" y SUMAR el monto de cada grupo
    #TAREA 1.3 ordenar de mayor a menor y retornar el resultado
    montos_validos = data_frame_gasto.query("monto > 0")

    resultado = (
        montos_validos
        .groupby("descripcion")["monto"]
        .sum()
        .reset_index(name="monto_total")
        .sort_values("monto_total", ascending=False)
    )

    return resultado


#EJERCICIO 2: PROMEDIO DE GASTO POR CATEGORIA (descripcion)   ->  MEAN
#GRAFICA QUE DEBE HACER EL ESTUDIANTE EN EL MAIN: grafica_barras
#   eje X = descripcion / eje Y = monto_promedio
#   (compara el gasto promedio de cada categoria -> barras)
def promedio_gasto_por_descripcion(data_frame_gasto):
    #TAREA 2.1 query: quedarse solo con los montos validos (monto > 0)
    #TAREA 2.2 groupby: agrupar por "descripcion" y sacar el PROMEDIO (mean) del monto
    #TAREA 2.3 ordenar de mayor a menor y retornar el resultado
    montos_validos = data_frame_gasto.query("monto > 0")

    resultado = (
        montos_validos
        .groupby("descripcion")["monto"]
        .mean()
        .reset_index(name="monto_promedio")
        .sort_values("monto_promedio", ascending=False)
    )

    return resultado


#EJERCICIO 3: CUANTOS GASTOS HIZO CADA USUARIO (id)   ->  COUNT
#GRAFICA QUE DEBE HACER EL ESTUDIANTE EN EL MAIN: grafica_torta
#   cada porcion = un usuario (id) / tamanio = cantidad_gastos
#   (muestra que proporcion de los gastos hizo cada usuario)
def cantidad_gastos_por_usuario(data_frame_gasto):
    #TAREA 3.1 query: quedarse solo con los gastos cuyo monto sea mayor a 0
    #TAREA 3.2 groupby: agrupar por "id" y CONTAR cuantos gastos tiene cada usuario
    #TAREA 3.3 ordenar de mayor a menor y retornar el resultado
    montos_validos = data_frame_gasto.query("monto > 0")

    resultado = (
        montos_validos
        .groupby("id")["monto"]
        .count()
        .reset_index(name="cantidad_gastos")
        .sort_values("cantidad_gastos", ascending=False)
    )

    return resultado


#EJERCICIO 4: GASTOS GRANDES POR CATEGORIA (filtro por monto)   ->  COUNT
#GRAFICA QUE DEBE HACER EL ESTUDIANTE EN EL MAIN: grafica_barras
#   eje X = descripcion / eje Y = cantidad_gastos_grandes
#   (compara cuantos gastos grandes hay en cada categoria -> barras)
def gastos_grandes_por_descripcion(data_frame_gasto):
    #TAREA 4.1 query: quedarse SOLO con los gastos grandes (por ejemplo monto > 100000)
    #TAREA 4.2 groupby: agrupar por "descripcion" y CONTAR cuantos gastos grandes hay
    #TAREA 4.3 ordenar de mayor a menor y retornar el resultado
    gastos_grandes = data_frame_gasto.query("monto > 100000")

    resultado = (
        gastos_grandes
        .groupby("descripcion")["id"]
        .count()
        .reset_index(name="cantidad_gastos_grandes")
        .sort_values("cantidad_gastos_grandes", ascending=False)
    )

    return resultado


#EJERCICIO 5: RESUMEN COMPLETO POR CATEGORIA   ->  COUNT + MEAN + SUM
#GRAFICA QUE DEBE HACER EL ESTUDIANTE EN EL MAIN: grafica_barras (una por metrica)
#   eje X = descripcion / eje Y = cada metrica:
#   cantidad_gastos, monto_promedio y monto_total (una grafica de barras por cada una)
def resumen_por_descripcion(data_frame_gasto):
    #TAREA 5.1 query: quedarse solo con los montos validos (monto > 0)
    #TAREA 5.2 groupby + agg: agrupar por "descripcion" y calcular a la vez:
    #          - cantidad_gastos -> count del id
    #          - monto_promedio  -> mean del monto
    #          - monto_total     -> sum del monto
    #TAREA 5.3 ordenar por monto_total de mayor a menor y retornar el resultado
    montos_validos = data_frame_gasto.query("monto > 0")

    resultado = (
        montos_validos
        .groupby("descripcion")
        .agg(
            cantidad_gastos=("id", "count"),
            monto_promedio=("monto", "mean"),
            monto_total=("monto", "sum"),
        )
        .reset_index()
        .sort_values("monto_total", ascending=False)
    )

    return resultado
