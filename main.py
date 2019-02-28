from abc_extension import ABCRegistrarMejores
from funcion_articulo_base import funcionArticuloBase
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot
from math import log
import numpy as np

# Parámetros para la obtención de resultados
optimo_esperado = 475062.4441
poblacion = 12
iteraciones = 50
ejecuciones = 30

resultados_ejecuciones = []
puntos_solucion_ejecuciones = []
valores_optimos_ejecuciones = []
promedios_mejores_soluciones_por_iteracion = []

# Ejecutar el algoritmo según el ńúmero de ejecuciones especificado
for i in range(ejecuciones):

    # Creación del objeto que representa el algoritmo a utilizar con los parámetros indicados
    algoritmoColoniaAbejasArtificiales = ABCRegistrarMejores(1, poblacion, iteraciones, funcionArticuloBase)

    # Ejecutar algoritmo y guardar respuesta
    valores_optimos_ejecuciones.append(algoritmoColoniaAbejasArtificiales.run())
    puntos_solucion_ejecuciones.append(algoritmoColoniaAbejasArtificiales.Best.Solution[0])
    
    # Guardar registro de cada iteración del algoritmo
    registros_mejores = algoritmoColoniaAbejasArtificiales.obtenerRegistros()
    
    # Extraer los mejores valores de cada iteración interna del algoritmo
    mejores_soluciones_por_iteracion = [registro[1] for registro in registros_mejores]

    # Agregar mejores soluciones por iteración de la ejecución actual a la lista que guarda los valores 
    # de todas las ejecuciones
    resultados_ejecuciones.append(mejores_soluciones_por_iteracion)

# Obtener promedio de la mejor solución en cada iteración
for i in range(iteraciones + 1):
    mejores_soluciones_iteracion_i = [resultado_ejecucion[i] for resultado_ejecucion in resultados_ejecuciones]
    promedios_mejores_soluciones_por_iteracion.append(np.mean(mejores_soluciones_iteracion_i))

# Crear y guardar gráfica de resultados
pyplot.axhline(y=optimo_esperado, color='r')
a = pyplot.plot(range(iteraciones + 1), promedios_mejores_soluciones_por_iteracion)
pyplot.subplots_adjust(left = 0.15)
pyplot.title('Promedios de la mejor solución en cada iteración para ' + str(ejecuciones) + ' ejecuciones')
pyplot.xlim(0, iteraciones)
pyplot.xlabel('Iteraciones')
limYInf = min(promedios_mejores_soluciones_por_iteracion + [optimo_esperado])
limYSup = max(promedios_mejores_soluciones_por_iteracion + [optimo_esperado])
pyplot.ylim(limYInf, limYSup)
pyplot.ylabel('Valor promedio de la función objetivo en la iteración')
pyplot.savefig('figuras/PromediosPorIteracionNEjecuciones.png')

# Imprimir promedio y desviación estándar de la respuesta del algoritmo (de las ejecuciones especificadas)
print("Promedio punto solución: " + str(np.mean(puntos_solucion_ejecuciones)))
print("Desviación estándar punto solución: " + str(np.std(puntos_solucion_ejecuciones)))
print("Promedio respuesta: " + str(np.mean(valores_optimos_ejecuciones)))
print("Desviación estándar de la respuesta: " + str(np.std(valores_optimos_ejecuciones)))
