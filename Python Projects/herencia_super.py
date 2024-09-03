class Persona():

	def __init__(self, nombre, edad, lugarResidencia):
		self.nombre = nombre
		self.edad = edad
		self.lugarResidencia = lugarResidencia

	def descripcion(self):
		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugarResidencia) 


class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugarResidencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, lugarResidencia_empleado)

		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ", self.salario, " Antiguedad: ", self.antiguedad)


manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")

manuel.descripcion()

print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))

