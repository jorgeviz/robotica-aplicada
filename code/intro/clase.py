"""
 Definición de un ejemplo de clase
"""


class MyClass(object):
	"""
           Documentación de Mi Clase
	   Atributos: i,hola, velocidad
           Métodos: 
		add_v()
                  - Params: Argumentos para suma
	"""

        # Variables de Clase 
	i = 'Variable de Clase'
	g = 9.8 # Gravedad

	# Método Constructor
	def __init__(self, vel):
                # Variables de instancia
		self.hola = 'variable de instancia'
		self.velocidad = vel

	# Método de Clase
	def add_v(self, *args):
		suma = self.velocidad
		for x in args:
			suma += x
		return suma

