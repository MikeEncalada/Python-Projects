miLista=["Maria", "Pepe", "Marta", "Antonio"]

print(miLista[:]) #Imprime toda la lista

print(miLista[2]) #Imprime solo el valor del indice

print(miLista[-1]) #Imprime el valor del índice al revez (Antonio)

print(miLista[0:3]) #Imprime el rango excluyendo el índice 3

print(miLista[:3]) #Interpreta que es 0 lo vacío

print(miLista[2:]) #Imprime desde el indice 2 hasta el final

miLista.append("Sandra") #Agrega otro elemento al final de la lista

miLista.insert(2, "Jose") #Agrega el elemento en el indice que se le indica

miLista.extend(["Luis", "Pedro"]) #Agrega varios elementos al final

print(miLista.index("Antonio")) #Devuelve el indice

print("Pedro" in miLista) #Devuelve un booleano si se encuentra o no en la lista

miLista2 = ["Jose", 7, 6.7, True] #Puede contener elementos de varios tipos

miLista2.remove(7) #Para eliminar el valor del elemento que se indica

miLista.pop() #Elimina el último valor de la lista

miLista3 = miLista + miLista2 #Concatena (une) las 2 lista

miLista4 = miLista * 3 #Una lista con tres veces la lista



