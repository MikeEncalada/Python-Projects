#Para distribuir los datos a través de bits

import pickle 

#Para volcar (guardar)

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_ binario = open("lista_nombres", "wb")  #wb --> Escritura binaria

pickel.dump(lista_nombres, fichero_binario) #La lista y el nombre del fichero en memoria (variable)

fichero_binario.close()

del(fichero_binario) #Se borra de memoria


#Para abrir

fichero = open("lista_nombres", "rb") #rv --> lectura binaria

lista = pickle.load(fichero)

print(lista)

