def crear_primos(limite=100000):
    """
    Genera una lista de números primos utilizando el método de prueba de divisibilidad.

    Args:
        limite (int): Cantidad de números a verificar para identificar primos. Por defecto es 100,000.

    Returns:
        list: Lista de números primos generados.
    """
    if limite < 2:
        return []

    primos = [2]  # Inicializar la lista de primos con el primer número primo
    n = 3

    while len(primos) < limite:
        es_primo = True
        max_divisor = int(n**0.5) + 1  # Solo necesitamos verificar hasta la raíz cuadrada de n

        for primo in primos:
            if primo > max_divisor:
                break  # Si el primo actual es mayor que la raíz cuadrada de n, no necesitamos seguir comprobando

            if n % primo == 0:
                es_primo = False
                break

        if es_primo:
            primos.append(n)

        n += 2  # Saltar números pares, ya que solo 2 es un primo par

    return primos
