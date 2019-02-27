from abc_extension import ABCRegistrarMejores
from funcion_articulo_base import funcionArticuloBase

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
print('Mejores soluciones: ' + str(registros_mejores))
print('Cantidad mejores: ' + str(len(registros_mejores)))