#Por defecto python busca los modulos en la misma carpeta sino está lo busca en el syspath
#Paquetes --> Directorios donde se alamcenarán módulos relacionados entre sí (Para organizar y reutilizar modulos)
#			  Para crearlos solo se crea una carpeta con un archivo __init__.py

from modulo_vehiculos import *

miCoche = Vehiculo("Mazda", "Cherry")

miCoche.estado()