from NiaPy.algorithms.basic import ArtificialBeeColonyAlgorithm
from NiaPy.algorithms.basic.abc import SolutionABC
import copy

class SolutionABCRegistrarMejores(SolutionABC):
	
	def __init__(self, solucionObjPadre, objABCRegistrarMejores):
		super().__init__(solucionObjPadre.D, solucionObjPadre.LB, solucionObjPadre.UB)
		self.Solution = solucionObjPadre.Solution
		self.Fitness = solucionObjPadre.Fitness
		self.objABCRegistrarMejores = objABCRegistrarMejores		
	
	def toString(self):
		self.objABCRegistrarMejores.registros.agregarRegistros(self.Solution, self.Fitness)
		self.objABCRegistrarMejores.aumentarContadorIteraciones()
		#print(str(self.Solution) + " " + str(self.Fitness))
		
	def __deepcopy__(self, memo):
		# Copia de los atributos de la superclase
		solucionABCCopia = SolutionABC(self.D, self.LB, self.UB)
		solucionABCCopia.Fitness = self.Fitness
		# Crear copia profunda del atributo Solution por ser una lista (objeto mutable)
		solucionABCCopia.Solution = copy.deepcopy(self.Solution, memo)
		# Crear copia
		solucionABCRegistrarMejoresCopia = SolutionABCRegistrarMejores(solucionABCCopia, self.objABCRegistrarMejores)
		return solucionABCRegistrarMejoresCopia

class ABCRegistrarMejores(ArtificialBeeColonyAlgorithm):
	
	def __init__(self, D, NP, iteraciones, benchmark):
		super().__init__(D, NP, None, benchmark)
		self.iteracion_actual = 0
		self.iteraciones = iteraciones
		self.registros = RegistroMejoresABC()
		
	def init(self):
		super().init()
		self.Best = SolutionABCRegistrarMejores(self.Best, self)
		for i in range(self.FoodNumber):
			self.Foods[i] = SolutionABCRegistrarMejores(self.Foods[i], self)
			self.checkForBest(self.Foods[i])
		# Si el valor de iteraciones es 0, dar por terminado el algoritmo
		if self.iteraciones == 0:
			self.Done = True
		
	def run(self):
		super().run()
		self.Best.toString()
		return self.Best.Fitness
		
	def tryEval(self, Solution):
		if type(Solution) == SolutionABC:
			indice = self.Foods.index(Solution)
			self.Foods[indice] = SolutionABCRegistrarMejores(Solution, self)
			self.Foods[indice].evaluate()
		else:
			Solution.evaluate()
		
		if self.FEs == self.nFES:
			self.Done = True
	
	def obtenerRegistros(self):
		return self.registros.obtenerRegistros()

	def aumentarContadorIteraciones(self):
		self.iteracion_actual += 1
		if self.iteracion_actual == self.iteraciones:
			self.Done = True		

class RegistroMejoresABC():
	
	def __init__(self):
		self.registros = ()
	
	def agregarRegistros(self, Solution, Fitness):
		self.registros = self.registros + ((Solution, Fitness),)
		# print(len(self.registros))
		
	def obtenerRegistros(self):
		return self.registros
		
		
		
	
	
	
	
		
	
	
	
	
	