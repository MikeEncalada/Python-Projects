#Paquetes distribuibles --> para crear e instalar paquetes en cualquier computador
#setup.py tiene la configuración

from setuptools import setup

setup(

	name = "paquetecalculos",
	vesrion = "1.0", #Lo que quieras
	description = "Paquete de redondeo y potencia",
	author = "Mike",
	author_email = "mike_tomas@hotmail.es",
	url = "www.mikeencalada.com",
	packages = ["calculos_pck"] # [Paquete, subpaquete] si es el caso o se utiliaz find.packages() para encontra automaticamente

	)

#CREACION
#Para crear el paquete distribuible se va al cmd como admin en la dirección del setup.py 
#se usa el comando: python setup.py sdist
#Se crean dos carpetas ([name].egg-info y dist)
#En dist nos encontramos con un archivo .tar.gz

#INSTALACION
#Para instalar en cualquier computadora, se va a la dirección donde está el .tar.gz
#Se abre el cmd y se coloca el comando: pip3 install [nombre del .tar.gz]

#DESINSTALACION
#En cualquier dirección
#pip3 uninstall [name]