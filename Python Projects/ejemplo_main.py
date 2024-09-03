def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.

    Parámetros:
    numero (float): El número del cual calcular la raíz cuadrada.

    Retorna:
    float: La raíz cuadrada del número.

    Raises:
    ValueError: Si se intenta calcular la raíz cuadrada de un número negativo.
    """
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

def main():
    # Aquí colocas el código principal de tu script
    numero = float(input("Ingrese un número: "))
    
    try:
        resultado = raiz_cuadrada(numero)
        print(f"La raíz cuadrada de {numero} es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 