class Vehiculo():

	def __init__(self, marca, modelo):
		self.marca = marca 
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ", self.marca,
		 "\nModelo: ", self.modelo,
		 "\nEn Marcha: ", self.enmarcha,
		 "\nAcelerando: ", self.acelera,
		 "\nFrenando: ", self.frena)

class Furgoneta(Vehiculo):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"


class Moto(Vehiculo):    #Para heredar solo se coloca dentro
	hcaballito = ""

	def caballito(self):
		self.hcaballito = "Voy haciendo el caballito"
 
	def estado(self):                    #Si creas el mismo metodo del padre este se sobreescribe
		print("Marca: ", self.marca,
		 "\nModelo: ", self.modelo,
		 "\nEn Marcha: ", self.enmarcha,
		 "\nAcelerando: ", self.acelera,
		 "\nFrenando: ", self.frena,
		 "\n", self.hcaballito)

class VElectricos(Vehiculo):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia = 100

	def cargarEnergia(self):
		self.cargando = True









