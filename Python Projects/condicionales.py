#Funcion IF

print("Programa de evaluacion de notas de alumnos")
nota_alumno = input("Introduzca la nota") #Para introducir valores por consola, es siempre String

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))


#Funcion IF - ELSE

print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100: #Es una mezcla de else - if
	print("Edad incorrecta")
else:
	print("Puedes pasar")

print("Edad del usuario: " + str(edad_usuario)) #No deja concatenar un string y un numero con + 


#Uso de operadores lógicos

if 5>4 or 6==5 and 7>4:
	print("correcto") 

#Funciones útiles

asignatura = "Informática gráfica"
opcion = asignatura.lower() #Para transformar todo a minusculas