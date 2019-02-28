from abc_extension import ABCRegistrarMejores
from funcion_articulo_base import funcionArticuloBase
from matplotlib import pyplot
from math import log
import numpy as np

lista = []
lista2 = list(range(1,31))
for i in range(30):
# Creación del objeto que representa el algoritmo a utilizar con los parámetros indicados
    poblacion = 4
    iteraciones = 5
    algoritmoColoniaAbejasArtificiales = ABCRegistrarMejores(1, poblacion, iteraciones, funcionArticuloBase)

# Ejecutar algoritmo
    valor_optimo = algoritmoColoniaAbejasArtificiales.run()

# Imprimir punto solución
    print('Punto solución: ' + str(algoritmoColoniaAbejasArtificiales.Best.Solution[0]))

# Imprimir valor óptimo
    print('Valor óptimo: ' + str(valor_optimo))

# Imprimir registro de los mejores valores para cada iteración
    registros_mejores = algoritmoColoniaAbejasArtificiales.obtenerRegistros()
  #  print('Mejores soluciones: ' + str(registros_mejores))
  #  print('Cantidad mejores: ' + str(len(registros_mejores)))
    y = [x[1] for x in registros_mejores]
    #print("promedio de x: " + str(np.mean(x)))
    #funcion que calcula el promedio 
    lista.append(np.mean(y))
print("promedio: " + str(np.mean(lista)))
print("desviacion estandar: " + str(np.std(lista)))
a = pyplot.plot(lista2,lista)
pyplot.axhline(y=475056, color='r')
pyplot.show()
