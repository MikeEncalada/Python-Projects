#Aplica una funcion a cada elemento de una lista iterable

class Empleado:

	def __init__(self, nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__(self):
		return "{} que trabaja como {} con salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
	Empleado("Juan", "Director", 6700),
	Empleado("Ana", "Presidenta", 7500),
	Empleado("Antonio", "Administrativo", 2100),
	Empleado("Sara", "Secretaria", 2150),
	Empleado("Mario", "Botones", 1800)
]

def calculo_comision(empleado):
	if(empleado.salario <= 3000):
		empleado.salario = empleado.salario * 1.03   #Posible error al hacer esto tambien cambia la listaEmpleado
	return empleado	

listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
	print(empleado)


for empleado in listaEmpleados:
	print(empleado)

