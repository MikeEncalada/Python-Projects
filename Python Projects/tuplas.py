#Las tuplas son inmutables (no se pueden modificar)
#Son más rápidas, menos espacio, se puede utilizar como clave en un diccionario

miTupla = ("Juan", 13, 1, 1995)

print(miTupla[2])

miLista = list(miTupla) #Para transformar una tupla en una lista

print(miLista)

miTupla2 = tuple(miLista) #Para transformar una lista en una tupla

print(miTupla.count(13)) #Cuenta cuantos valores existen

print(len(miTupla)) #Cuenta cuantos elementos

miTupla3 = ("Juan",) #Para una tupla unitaria

miTupla4 = "Juan", 13, 1, 1995 #Sin parentesis sigue siendo tupla (Empaquetado de tupla)

miTupla5 = ("Juan", 13, 1, 1995)
nombre, dia, mes, anio = miTupla5 #Le da los valores a cada una de las variables (Desempaquetado de tupla)