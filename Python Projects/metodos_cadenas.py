nombreUsuario = input("Introduce tu nombre de Usuario: ")

print("El nombre es: ", nombreUsuario)

nombreUsuario.upper() #Cambia todos los caracteres a mayúsculas

nombreUsuario.lower() #Cambia todos los caracteres a minúsculas

nombreUsuario.capitalize() #La primera letra en mayúsculas

edad = input("Introduce la edad: ")

while(edad.isdigit() == False):
	print("Por favor introduce un valor numérico")

	edad =  input("Introduce la edad: ")


#Devuelve true o false si el String es un número

if(int(edad) < 18):
	print("No puede pasar")
else:
	print("Puede pasar")
