#Tienen una estructura de clave:valor
#Los elementos no están ordenados
#No se puede tener dos claves iguales

miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}

print(miDiccionario["Francia"]) #Se coloca la clave del elemento

miDiccionario["Italia"] = "Lisboa" #Para agregar otro elemento

miDiccionario["Italia"] = "Roma" #Para modificar un elemento (modifica no agrega si existe ya la clave)

del miDiccionario["Reino Unido"] #Para eliminar la clave:valor del diccionario

miDiccionario1 = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3} #Se puede alternar los tipos

miTupla = ("España", "Francia", "Reino Unido", "Alemania")
miDiccionario2={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"} #Se puede utilizar una tupla como clave
print(miDiccionario2["Francia"])

miDiccionario3 = {23:"Jordan", "Nombre":"Michel", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]} #Puede guardar tuplas y lista como valores
print(miDiccionario3["Anillos"])

miDiccionario4 = {23:"Jordan", "Nombre":"Michel", "Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}} #Puede guardar diccionarios

print(miDiccionario.keys()) #Imprime todas las llaves existentes 

print(miDiccionario.values()) #Imprime todas los valores existentes 

print(len(miDiccionario)) #Devuelve el numero de valores existentes 