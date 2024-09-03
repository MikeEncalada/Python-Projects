#Modularizacion --> una aplicacion puede estar compuesta por varias clases
#Encapsulación --> lógica que únicamente la clase conoce (Está protegido del exterior)


class Coche():

	def __init__(self):          #Constructor
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4        #__ --> Para que no sea accesible (private)
		self.__enMarcha = False

	def arrancar(self, arrancamos):  #Con self se refiere que es un método de la clase, self hace referencia a la instancia referente a la clase (this)
		self.__enMarcha = arrancamos

		if (self.__enMarcha):
			chequeo = self.__chequeo_interno()

		if(self.__enMarcha and chequeo):
			return "El coche está en marcha"
		elif(self.__enMarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo"
		else:
			return "El coche esta parado"


	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis,  " y un largo de ", #Con coma se puede concatenar Strings con numeros
			self.__largoChasis)

	def __chequeo_interno(self):             # __ --> Igualmente para que no sea accesible desde el exterior (private)
		print("Realizando chequeo interno")
		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
			return True
		else:
			return False


miCoche = Coche() #Instanciar una clase

print(miCoche.arrancar(True))

miCoche.estado()


print("-----------------A continuación creamos el segundo objeto--------------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

#miCoche2.ruedas = 5  # Si se puede modificar está mal

miCoche2.estado()



