def divide():

	try:

		op1=(float(input("Introduce el primer numero: ")))

		op2=(float(input("Introduce el segundo numero: ")))

		print("La división es:" + str(op1/op2))

	except ValueError:
		print("El valor introducido es erroneo")

	except ZeroDivisionError as ErrorDeDivisionCero:
		print(ErrorDeDivisionCero) #Imprime el mensaje del error
		print("No se puede dividir entre 0")
	
	except: #Captura un error general
		print("Ha ocurrido un error")

	finally: #Ejecuta estas instrucciones siempre, se puede colocar esto sin catchs (da el error pero se ejecuta esto antes)
		print("Calculo finalizado")

divide()




def evaluaEdad(edad):
	if edad < 0:
		raise TypeError("No se permiten edades negativas") #Lanzamiento de excepciones

	if edad < 20:
		return "eres muy joven"
	elif edad < 40:
		return "eres joven"
	elif edad < 65:
		return "eres maduro"
	elif edad < 100:
		return "Cuidate...."


print(evaluaEdad(70))