#Estrucuturas que se extraen de una función y se almacenan en un iterable (Se almacenan de uno a uno)
#Más eficientes que las funciones tradicionales
#Para valores infinitos o grandes


#Función tradicional
def generarPares(limite):
	num = 1
	miLista = []

	while num < limite:
		miLista.append(num * 2)
		num = num + 1

	return miLista


print(generarPares(10))


#Generador
def generarPares1(limite):
	num = 1

	while num < limite:
		yield num * 2
		num = num + 1

devuelvePares = generaPares1(10)

""" Con esto imprime toda la lista con todos los valores
for i in devuelvePares:
	print(i)
"""

#Esto Devuelve solo los 3 primeros

print(next(devuelvePares)) #Vuelve a la linea 29

print("Aqui podría ir mas codigo ....")

print(next(devuelvePares)) #Vuelve a la linea 29

print("Aqui podría ir mas codigo ....")

print(next(devuelvePares)) #Vuelve a la linea 29



#Yield from --> Simplifica el código de los generadores en el caso de utilizar bucles anidados


def devulveCiudades(*ciudades): #Para dar un numero indeterminado de elementos, pero en forma de TUPLA
	for elemento in ciudades:
		#for subElemento in elemento: 
		yield from elemento #Hace lo mismo si se utiliza el for de arriba 

ciudades_devueltas = devulveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas)) #(Da los primeros letras del primer elemento "M a")







