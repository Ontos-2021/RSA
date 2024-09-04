def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) entre dos números usando el Algoritmo de Euclides.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: El MCD de a y b.
    """
    while b != 0:
        a, b = b, a % b  # Actualiza a con b y b con el residuo de a/b
    return a


def factorizar(numero):
    """
    Calcula los factores primos de un número.

    Args:
        numero (int): Número a factorizar.

    Returns:
        list: Lista de factores primos del número.
    """
    divisores = []
    i = 2

    while i * i <= numero:  # Solo es necesario verificar hasta la raíz cuadrada del número
        while numero % i == 0:
            divisores.append(i)
            numero //= i  # Actualiza el número dividiéndolo por el factor encontrado
        i += 1

    if numero > 1:  # Si queda algún factor primo mayor que la raíz cuadrada
        divisores.append(numero)

    return divisores
