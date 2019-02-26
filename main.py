from abc_extension import ABCRegistrarMejores
from funcion_articulo_base import funcionArticuloBase

# Creación del objeto que representa el algoritmo a utilizar con los parámetros indicados
algoritmoColoniaAbejasArtificiales = ABCRegistrarMejores(1, 4, 22, funcionArticuloBase)

# Ejecutar algoritmo
valor_optimo = algoritmoColoniaAbejasArtificiales.run()

# Imprimir punto solución
print('Punto solución: ' + str(algoritmoColoniaAbejasArtificiales.Best.Solution[0]))

# Imprimir valor óptimo
print('Valor óptimo: ' + str(valor_optimo))

print(algoritmoColoniaAbejasArtificiales.obtenerRegistros())