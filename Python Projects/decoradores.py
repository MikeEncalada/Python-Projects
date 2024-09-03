#Los decoradores decoran funciones
""" Ejemplo simple
def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		#Acciones adicionales que decoran
		print("Vamos a realizar un calculo: ")
		funcion_parametro()
		#Acciones adicionales que decoran
		print("Hemos terminado el calculo.")

	return funcion_interior

@funcion_decoradora    #Para decorar esta función
def suma():
	print(15 + 20)

def resta():
	print(30 - 10)




suma()

resta()
"""


def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs):                  #** --> Para parametros clave valor es decir un llamado potencia(base=5, exponente=3)
		#Acciones adicionales que decoran
		print("Vamos a realizar un calculo: ")
		funcion_parametro(*args, **kwargs)
		#Acciones adicionales que decoran
		print("Hemos terminado el calculo.")

	return funcion_interior

@funcion_decoradora    #Para decorar esta función
def suma(num1, num2, num3):
	print(num1 + num2 + num3)

@funcion_decoradora 
def resta(num1, num2):
	print(num1 - num2)

@funcion_decoradora 
def potencia(base, exponente):
	print(base ** exponente) 


suma(7, 5, 8)

resta(12, 10)

potencia(base=5, exponente=3)