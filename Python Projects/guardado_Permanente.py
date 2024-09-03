import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona nueva con el nombre: ", self.nombre)

	def __str__(self):    #toString()
		return "{} {} {}".format(self.nombre, self.genero, self.edad) #Para formatear un String

class ListaPersonas:

	personas = []

	def __init__(self):
		listaDePersonas = open("ficheroExterno", "ab+")  #Agregar información binaria
		listaDePersonas.seek(0) #Para desplazarse a la posición 0 del fichero
		try:
			self.personas = pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero está vacío.")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas = open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInformacionFicheroExterno(self):
		print("La información del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)


miLista = ListaPersonas()
persona = Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(persona)
miLista.mostrarInformacionFicheroExterno()


