"""En funciones
def areaCuadrado(lado):
		Calcula el area de un cuadrado
		elevando al cuadrado el lado pasado por parámetro
	
	return "El area del cuadrado es: " + str(lado * lado)  

def areaTriangulo(base, altura):
	
		Calcula el area de un triangulo utilizando los parametros base y altura
	
	return "El area del triangulo es: " + str((base * altura) / 2)  

print(areaCuadrado(5))
print(areaCuadrado.__doc__) #Imprime los comentarios (documentacion) de esa función
help(areaCuadrado) # Ofrece información más detallada que arriba 

"""

class Areas: 

	"""
		Esta clase calcula las areas de diferentes figuras geometricas
	"""

	def areaCuadrado(lado):
		"""
			Calcula el area de un cuadrado
			elevando al cuadrado el lado pasado por parámetro
		"""
		return "El area del cuadrado es: " + str(lado * lado)  

	def areaTriangulo(base, altura):
		"""
			Calcula el area de un triangulo utilizando los parametros base y altura
		"""
		return "El area del triangulo es: " + str((base * altura) / 2)  

#print(areaCuadrado(5))
#print(areaCuadrado.__doc__) #Imprime los comentarios (documentacion) de esa función
help(Areas.areaCuadrado) # Ofrece información más detallada que arriba 
help(Areas)

#Tambien se puede poner en modulos
#help([nombre del modulo])

 
	
	
