from NiaPy.algorithms.basic import ArtificialBeeColonyAlgorithm
from NiaPy.algorithms.basic.abc import SolutionABC
import copy

class SolutionABCRegistrarMejores(SolutionABC):
	'''
	Clase que representa una solución particular del algoritmo de la Colonia
	de Abejas Artificiales la cual guarda su representación cuando su método
	toString es llamado y modifica como se realizan copias profundas de sí misma.
	'''
	
	def __init__(self, solucionObjPadre, objABCRegistrarMejores):
		'''
		Constructor de la solucion particular del algoritmo extendido.
		Args:
			solucionObjPadre (SolutionABC): solución particular usada por el algoritmo de NiaPy.
			objABCRegistrarMejores (ABCRegistrarMejores): objeto que representa al algoritmo extendido.
		'''
		super().__init__(solucionObjPadre.D, solucionObjPadre.LB, solucionObjPadre.UB)
		self.Solution = solucionObjPadre.Solution
		self.Fitness = solucionObjPadre.Fitness
		self.objABCRegistrarMejores = objABCRegistrarMejores		
	
	def toString(self):
		'''
		Método que se encarga de guardar la representación de la solución particular representada
		por el presente objeto y de aumentar el contador del algoritmo, pues su llamada indica
		el inicio de una nueva iteración del mismo.
		'''
		self.objABCRegistrarMejores.registros.agregarRegistros(self.Solution, self.Fitness)
		self.objABCRegistrarMejores.aumentarContadorIteraciones()
		#print(str(self.Solution) + " " + str(self.Fitness))
		
	def __deepcopy__(self, memo):
		'''
		Método que modifica la forma como se realizar copias profundas de los objetos de la
		presente clase, con el fin de que estos compartan la referencia al algoritmo
		que los creó (un objeto de tipo ABCRegistrarMejores).
		Args:
			memo (dict): diccionario que permite rastrear cuáles objetos ya han sido copiados.
		'''
		# Copia de los atributos de la superclase
		solucionABCCopia = SolutionABC(self.D, self.LB, self.UB)
		solucionABCCopia.Fitness = self.Fitness
		# Crear copia profunda del atributo Solution por ser una lista (objeto mutable)
		solucionABCCopia.Solution = copy.deepcopy(self.Solution, memo)
		# Crear copia
		solucionABCRegistrarMejoresCopia = SolutionABCRegistrarMejores(solucionABCCopia, self.objABCRegistrarMejores)
		return solucionABCRegistrarMejoresCopia

class ABCRegistrarMejores(ArtificialBeeColonyAlgorithm):
	'''
	Clase que representa la versión extendida de la implementación en NiaPy
	del algoritmo de Colonia de Abejas Artificiales, el cual realiza 2 modificaciones:
	- Controla la terminación del algoritmo en función de un número límite de iteraciones
	  y no de un número de evaluaciones de la función objetivo.
	- Registra la mejor solución encontrada en cada iteración del algoritmo.
	'''
	
	def __init__(self, D, NP, iteraciones, benchmark):
		'''
		Constructor del objeto que representa el algoritmo.
		Args:
			- D (int): dimensión del problema.
			- NP (int): tamaño de la colonia.
			- iteraciones (int): número de iteraciones del algoritmo.
			- benchmark: función a optimizar.
		'''
		super().__init__(D, NP, None, benchmark)
		self.iteracion_actual = 0
		self.iteraciones = iteraciones
		self.registros = RegistroMejoresABC()
		
	def init(self):
		'''
		Función que se encarga de cambiar el tipo de las soluciones aleatorias
		creadas y de la mejor hallada hasta el momento de SolutionABC a
		SolutionABCRegistrarMejores.
		'''
		super().init()
		self.Best = SolutionABCRegistrarMejores(self.Best, self)
		for i in range(self.FoodNumber):
			self.Foods[i] = SolutionABCRegistrarMejores(self.Foods[i], self)
			self.checkForBest(self.Foods[i])
		# Si el valor de iteraciones es 0, dar por terminado el algoritmo
		if self.iteraciones == 0:
			self.Done = True
		
	def run(self):
		'''
		Extiende el método run() de ArtificialBeeColonyAlgorithm al registrar
		el mejor valor de la mejor solución hallada en todo el algoritmo.
		Returns:
			float: El valor en la función a optimizar del mejor punto solución
				   encontrado por el algoritmo.
		'''
		super().run()
		self.Best.toString()
		return self.Best.Fitness
		
	def tryEval(self, Solution):
		'''
		Convierte al tipo correcto la solución creada por la abeja exploradora,
		además de evaluar la solución pasada como argumento.
		Args:
			Solution ([float]): solución a evaluar en la función a optimizar.
		'''
		if type(Solution) == SolutionABC:
			indice = self.Foods.index(Solution)
			self.Foods[indice] = SolutionABCRegistrarMejores(Solution, self)
			self.Foods[indice].evaluate()
		else:
			Solution.evaluate()
	
	def obtenerRegistros(self):
		'''
		Devuelve los registros de las mejores soluciones halladas en cada iteración
		del algoritmo:
		Returns:
			(([float], float),): tupla de tuplas con el mejor valor 
		'''
		return self.registros.obtenerRegistros()

	def aumentarContadorIteraciones(self):
		'''
		Método que aumenta el número de la iteración actual hasta que es
		igual al número de iteraciones especificado al momento de crear el
		objeto del algoritmo, condición que finaliza el algoritmo cuando se 
		termina la iteración actualmente en ejecución.
		'''
		self.iteracion_actual += 1
		if self.iteracion_actual == self.iteraciones:
			self.Done = True		

class RegistroMejoresABC():
	'''
	Clase cuyos objetos registran las mejores soluciones en cada iteración del
	algoritmo.
	'''
	
	def __init__(self):
		'''
		Constructor que inicializa la estructura de datos que va a guardar las mejores
		soluciones en cada iteración del algoritmo.
		'''
		self.registros = ()
	
	def agregarRegistros(self, Solution, Fitness):
		'''
		Método que añade la mejor solución de una nueva iteración del algoritmo
		al final del registro que lleva:
		Args:
			Solution ([float]): punto solución de la mejor solución en la iteración.
			Fitness (float): valor del punto solución de la mejor solución en la iteración
							 en la función a optimizar.
		'''
		self.registros = self.registros + ((Solution, Fitness),)
		# print(len(self.registros))
		
	def obtenerRegistros(self):
		'''
		Retorna los registros de las mejores soluciones encontradas.
		Returns:
			(([float], float)): estructura de datos con las mejores soluciones halladas 
								hasta el momento.
		'''
		return self.registros
		
		
		
	
	
	
	
		
	
	
	
	
	