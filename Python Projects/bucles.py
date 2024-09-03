
#Bucle FOR

for i in [1, 2, 3]: #Se puede colocar listas, tuplas, Strings
	print("Hola")

for i in ["Verano", "Invierno", "Otoño", "Primavera"]: #i toma el valor de cada uno de los elementos
	print(i)

for i in ["Pildoras", "Informaticas", 3]:
	print("Hola", end=" ") #Se le dice como se quiere que termine cada impresión (por defecto \n)

for i in "juan@Pildorasinformaticas.es": #Se repite por la cantidad de caracteres del STRING
	print(i)

for i in range(5): #Como una lista de 0 a 4
	print(f"Valor de la variable {i}") #Para formatear 

for i in range(5,10) #Del 5 al 9
	print(i)

for i in range(5,50,3) #Del 5 al 49 saltando de 3 en 3
	print(i)


#Bucle WHILE
i = 1

while i<=10:
	print("Ejecución " + str(i))
	i = i + 1
	if i == 5:
		print("Demasiandos intentos")
		break #Para romper el bucle


#continue --> Pasa a la siguiente iteración del bucle
#pass --> Devolver un null (Si quieres hacer una clase nula o si quieres instanciar un bucle pero no quieres hacerlo aún)
#else --> Igual que con if


for letra in "Python":
	if letra == "h":
		continue

	print ("Viendo la letra: " + letra)


while True: 
	pass #Como un ctrl + c

class MiClase:
	pass







