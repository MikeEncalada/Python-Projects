
import pickle

#Para leer necesitamos importar la clase 

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
	print(c.estado())