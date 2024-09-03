
#Las funciones lambda o anonimas permite simplificar la sintaxis de la funcion
#Solo para funciones simples, no permite condicionales, bucles, ....

"""FUNCION TRADICIONAL
def area_triangulo(base, altura):
	return (base * altura) / 2

triangulo1 = area_triangulo(5,7)

triangulo2 = area_triangulo(9,6)

print(triangulo1)

print(triangulo2)
"""

area_triangulo = lambda base,altura: (base * altura) / 2

print(area_triangulo(7,5))

triangulo1 = area_triangulo(9,6)

print(triangulo1)


#Puede servir para formatear Strings

destacar_valor = lambda comision:"!{}! $".format(comision) 