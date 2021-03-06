import math

class FuncionArticuloBase(object):
    '''
    Esta clase implementa el "benchmark" (término que en NiaPy se refiera a una
    función que se desea optimizar) personalizado que representa
    la función a optimizar del artículo "Desarrollo de un modelo para determinar 
    el lote óptimo de producción mediante programación no lineal y propuesta de su 
    resolución con una hoja de cálculo", desarrollado por Javier Valencia, María Pilar Lambán 
    y Jesús Royo.
    '''

    def __init__(self, param):
        '''
        Constructor que inicializa la función con sus límites y parámetros.
        Args:
            param (dict{str:float}): parámetros de la función
        '''
        # Se define el límite inferior de la función
        self.Lower = 0.000001
        # Se define el límite superior de la función
        self.Upper = 3361.3
        # Se guardan los parámetros de la función
        self.param = param

    def function(self):
        '''
        Función que retorna otra función que calcula el valor de la función
        a optimizar
        Returns:
            func([float], float): función que evalúa [float] en la función a optimizar.
                                  [float] solo puede tener 1 elemento, puesto que la
                                  función es de 1 variable.
        '''
        def evaluate(D, sol):

            # Revisar integridad de los argumentos
            if D != 1:
                raise ValueError("El argumento D debe ser igual a 1")
            elif len(sol) != 1:
                raise ValueError("El argumento sol debe contener solo 1 elemento")
            
            sol = sol[0]
            val = 0.0
            val = self.param["l"] * self.param["r"] / (1 - self.param["teta1"] * self.param["x"])\
                + self.param["l"] * self.param["K"] / (sol * (1 - self.param["teta1"] * self.param["x"]))\
                    + self.param["l"] * self.param["C"] * self.param["utp"] / (1 - self.param["teta1"] * self.param["x"])\
                        + self.param["l"] * self.param["Cr"] * self.param["x"] * self.param["utr"] / (1 - self.param["teta1"] * self.param["x"])\
                            + self.param["l"] * self.param["Cs"] * self.param["x"] * self.param["teta1"] / (1 - self.param["teta1"] * self.param["x"])\
                                + self.param["l"] * self.param["n"] * math.ceil((sol * (1 - self.param["teta1"] * self.param["x"]) / (self.param["n"] * self.param["capt"]))) * self.param["K1"] / (sol * (1 - self.param["teta1"] * self.param["x"]))\
                                    + self.param["l"] * self.param["ilogt"] * (self.param["Ct"] + self.param["Cti"])\
                                        + (self.param["l"] * self.param["iloga"] / (1 - self.param["teta1"] * self.param["x"])) * ((sol - 1) * self.param["h"] * self.param["utp"] / 2 + self.param["h1"] * (sol * self.param["utr"] * self.param["x"]**2 - self.param["utr"] * self.param["x"] * (sol * self.param["x"] + 1) / 2) + sol * self.param["h"] * (1 - self.param["x"]) * self.param["x"] * self.param["utr"] + self.param["h"] * self.param["utr"] * self.param["x"] * (sol * self.param["x"] - 1) / 2 + self.param["h"] * (self.param["n"] - 1) * (1 - self.param["teta1"] * self.param["x"]) * (((sol / self.param["l"]) * (1 - self.param["x"] * self.param["teta1"])) - sol * self.param["utp"] - sol * self.param["x"] * self.param["utp"]) / (2 * self.param["n"]))\
                                            + self.param["l"] * (self.param["M"] + self.param["M"] * self.param["x"] + self.param["N"] + self.param["N"] * self.param["x"]) / (1 - self.param["teta1"] * self.param["x"])
            return val
        return evaluate

# Definición de los parámetros de la función a optimizar
param = {}
param["l"] = 3400
param["P"] = 60000
param["x"] = 0.15
param["teta1"] = 0.1
param["P1"] = 2200
param["n"] = 4
param["utp"] = 0.5
param["utr"] = 0.8
param["iloga"] = 0.7
param["ilogt"] = 0.5
param["T"] = 2.35
param["capt"] = 1000
param["capA1"] = 3000
param["capA2"] = 2000
param["capA3"] = 2000
param["capA4"] = 10000
#########
param["K"] = 20000
param["C"] = 200
param["Cr"] = 120
param["Cs"] = 20
param["K1"] = 4350
param["Ct"] = 0.10
param["Cti"] = 0.05
param["h1"] = 0.0023
param["h"] = 0.0046
param["M"] = 0.05
param["N"] = 0.01
param["r"] = 10

# Creación del objeto que representa la función a optimizar
funcionArticuloBase = FuncionArticuloBase(param)