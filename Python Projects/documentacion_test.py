
"""
def areaTriangulo(base, altura):

	
	#Calcula el area de un triangulo dado

	#>>> areaTriangulo(3, 6)
	#9.0

	#>>> areaTriangulo(9,3)
	#13.5

	

	return (base * altura) / 2

import doctest
doctest.testmod() 
#Si no devuelve nada entonces no hay ningun error
#Para Strings se utiliza comillas simples ''
"""


def compruebaMail(mailUsuario):
	"""
	La funcion compruebaMail evalua un mail
	recibido en busca de la @. Si tiene una @
	es correcto, si tiene más de un @ es incorrecto
	si la @ está al final es incorrecto

	>>> compruebaMail('juan@cursos.es')
	True

	>>> compruebaMail('juancursos.es@')
	False

	>>> compruebaMail('juancursos.es')
	False

	>>> compruebaMail('juan@cursos@.es')
	False

	"""

	arroba = mailUsuario.count('@')
	if(arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario) - 1) or mailUsuario.find('@') == 0):
		return False
	else:
		return True


import doctest
doctest.testmod() 