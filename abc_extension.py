from NiaPy.algorithms.basic import ArtificialBeeColonyAlgorithm
from NiaPy.algorithms.basic.abc import SolutionABC

class SolutionABCRegistrarMejores(SolutionABC):
	
	def __init__(self,solucionObjPadre,registrosMejores):
		super().__init__(solucionObjPadre.D, solucionObjPadre.LB, solucionObjPadre.UB)
		self.Solution = solucionObjPadre.Solution
		self.Fitness = solucionObjPadre.Fitness
		self.registrosMejores = registrosMejores
	
	def toString(self):
		self.registrosMejores.agregarRegistros(self.Solution, self.Fitness) 
		#print(str(self.Solution) + " " + str(self.Fitness))
		
	def __deepcopy__(self):
		

class ABCRegistrarMejores(ArtificialBeeColonyAlgorithm):
	
	def __init__(self, D, NP, nFES, benchmark):
		super().__init__(D, NP, nFES, benchmark)
		self.registros = RegistroMejoresABC()
		self.Best = SolutionABCRegistrarMejores(self.Best, self.registros)
		
	def init(self):
		super().init()
		for i in range(self.FoodNumber):
			self.Foods[i] = SolutionABCRegistrarMejores(self.Foods[i], self.registros)
			self.checkForBest(self.Foods[i])
		
	def run(self):
		super().run()
		self.Best.toString()
		return self.Best.Fitness
		
	def tryEval(self, Solution):
		if type(Solution) == SolutionABC:
			indice = self.Foods[self.Foods.index(Solution)]
			self.Foods[indice] = SolutionABCRegistrarMejores(Solution, self.registros)
			super().tryEval(self.Foods[indice])
		else:
			super().tryEval(Solution)
	
	def obtenerRegistros(self):
		return self.registros.obtenerRegistros()
		
			

class RegistroMejoresABC():
	
	def __init__(self):
		self.registros = ()
	
	def agregarRegistros(self, Solution, Fitness):
		self.registros = self.registros + ((Solution, Fitness),)
		print(len(self.registros))
		
	def obtenerRegistros(self):
		return self.registros
		
		
		
	
	
	
	
		
	
	
	
	
	