import os
import shutil
import pandas as pd

from notebook.descripcion.descripcionUsuario import consumir_api_usuarios
from notebook.descripcion.descripcionGasto import consumir_api_gastos

from notebook.limpieza.limpiezaUsuario import limpiar_datos_usuario
from notebook.limpieza.limpiezaGasto import limpiar_datos_gasto

from notebook.transformacion.transformarUsuario import promedio_edad_por_correo
from notebook.transformacion.transformarUsuario import suma_edades_jovenes_por_nombre
from notebook.transformacion.transformarUsuario import usuarios_por_edad_en_rango
from notebook.transformacion.transformarUsuario import resumen_por_nombre
from notebook.transformacion.transformarUsuario import usuarios_adultos_por_nombre
from notebook.transformacion.transformacionGasto import total_gastado_por_descripcion
from notebook.transformacion.transformacionGasto import promedio_gasto_por_descripcion
from notebook.transformacion.transformacionGasto import cantidad_gastos_por_usuario
from notebook.transformacion.transformacionGasto import gastos_grandes_por_descripcion
from notebook.transformacion.transformacionGasto import resumen_por_descripcion

from notebook.reportes.graficasGenericas import grafica_barras,grafica_linea,grafica_torta,_mostrar_o_guardar


#Rutina de analis de datos de usuarios
#1. Consumo del api para obtener los datos crudos
datos_usuarios=consumir_api_usuarios()

#2. Creando un data frame con los datos del usuario
datos_usuarios_df=pd.DataFrame(datos_usuarios)

#3. Limpiamos los datos
datos_usuarios_limpios=limpiar_datos_usuario(datos_usuarios_df)

#4. Transformar los datos para generar las agrupaciones
adultos=usuarios_adultos_por_nombre(datos_usuarios_limpios)
promedio_correo=promedio_edad_por_correo(datos_usuarios_limpios)
suma_jovenes=suma_edades_jovenes_por_nombre(datos_usuarios_limpios)
usuarios_por_edad=usuarios_por_edad_en_rango(datos_usuarios_limpios)
resumen=resumen_por_nombre(datos_usuarios_limpios)


#5. Con las tarnsformaciones graficamos
#Grafica 1
carpeta_graficas="graficas"
os.makedirs(carpeta_graficas,exist_ok=True)

grafica_barras(adultos["nombres"],adultos["cantidad_usuarios"],"cantidad de usuarios por nombre","nombres","cantidad usuarios",os.path.join(carpeta_graficas,"grafica1.png"))

#Grafica2
grafica_barras(promedio_correo["correo"],promedio_correo["edad_promedio"],"Edad promedio por correo", "Correo","Edad promedio",os.path.join(carpeta_graficas,"grafica2.png"))

#Grafica 3
grafica_torta(suma_jovenes["nombres"],suma_jovenes["suma_edades"],"suma de edades de usuarios jovenes por nombre",os.path.join(carpeta_graficas,"grafica3.png"))

#Grafica 4
grafica_linea(usuarios_por_edad["edad"],usuarios_por_edad["cantidad_usuarios"], "cantidad de usuarios por edad","Edad","Cantidad",os.path.join(carpeta_graficas,"grafica4.png"))

#Grafica 5
grafica_barras(resumen["nombres"],resumen["cantidad_usuarios"],"Resumen por nombre","Nombres","Cantidad",os.path.join(carpeta_graficas,"grafica5.png"))


#Rutina de analisis de datos de gastos
datos_gastos=consumir_api_gastos()

datos_gastos_df=pd.DataFrame(datos_gastos)

datos_gastos_limpios=limpiar_datos_gasto(datos_gastos_df)

total_por_descripcion=total_gastado_por_descripcion(datos_gastos_limpios)
promedio_por_descripcion=promedio_gasto_por_descripcion(datos_gastos_limpios)
cantidad_por_usuario=cantidad_gastos_por_usuario(datos_gastos_limpios)
gastos_grandes=gastos_grandes_por_descripcion(datos_gastos_limpios)
resumen_descripcion=resumen_por_descripcion(datos_gastos_limpios)

#Grafica 6
grafica_barras(total_por_descripcion["descripcion"],total_por_descripcion["monto_total"],"total gastado por descripcion","descripcion","monto total",os.path.join(carpeta_graficas,"grafica6.png"))

#Grafica 7
grafica_barras(promedio_por_descripcion["descripcion"],promedio_por_descripcion["monto_promedio"],"promedio de gasto por descripcion","descripcion","monto promedio",os.path.join(carpeta_graficas,"grafica7.png"))

#Grafica 8
top_usuarios_gastos = (
	cantidad_por_usuario
	.sort_values("cantidad_gastos", ascending=False)
	.head(10)
)
grafica_barras(top_usuarios_gastos["id"],top_usuarios_gastos["cantidad_gastos"],"cantidad de gastos por usuario (top 10)","usuario","cantidad de gastos",os.path.join(carpeta_graficas,"grafica8.png"))

#Grafica 9
grafica_barras(gastos_grandes["descripcion"],gastos_grandes["cantidad_gastos_grandes"],"gastos grandes por descripcion","descripcion","cantidad gastos grandes",os.path.join(carpeta_graficas,"grafica9.png"))

#Grafica 10
grafica_barras(resumen_descripcion["descripcion"],resumen_descripcion["monto_total"],"resumen por descripcion","descripcion","monto total",os.path.join(carpeta_graficas,"grafica10.png"))


#Copia de imagenes para frontend (si existe estructura web)
ruta_public_graficas = os.path.join("public", "graficas")
os.makedirs(ruta_public_graficas, exist_ok=True)

for nombre_archivo in os.listdir(carpeta_graficas):
	if nombre_archivo.lower().endswith(".png"):
		origen = os.path.join(carpeta_graficas, nombre_archivo)
		destino = os.path.join(ruta_public_graficas, nombre_archivo)
		shutil.copy2(origen, destino)



