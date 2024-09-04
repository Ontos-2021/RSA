import math
from random import randint
from PRIMOS.primos import crear_primos  # Importa la función para generar números primos
from MCD.MCD import mcd  # Importa la función para calcular el máximo común divisor


def elegir_primo(primos, pi_n=None):
    """
    Selecciona un número primo al azar de la lista de primos.
    Si pi_n se proporciona, asegura que el MCD del número primo seleccionado y pi_n sea 1.

    Args:
        primos (list): Lista de números primos.
        pi_n (int, opcional): Valor de pi(n) para validar el MCD. Si no se proporciona, se ignora la validación.

    Returns:
        int: Número primo seleccionado.
    """
    while True:
        primo = primos[randint(len(primos) // 2, len(primos) - 1)]  # Selecciona un primo aleatorio de la mitad superior
        if pi_n is None or mcd(primo, pi_n) == 1:  # Verifica la condición del MCD si se proporciona pi_n
            return primo


def calcular_d(e, pi_n):
    """
    Calcula el valor de 'd' para la llave privada utilizando la congruencia lineal.

    Args:
        e (int): Componente 'e' de la llave pública.
        pi_n (int): Valor de pi(n).

    Returns:
        int: El valor de 'd' que satisface la ecuación de congruencia.
    """
    for k in range(1, pi_n):
        d = (1 + k * pi_n) // e
        if (e * d) % pi_n == 1:
            return d
    raise ValueError("No se pudo encontrar un valor adecuado para 'd'.")


# Paso 1: Crear números primos P y Q
primos = crear_primos()  # Genera una lista de números primos

# Selecciona dos números primos P y Q
p = elegir_primo(primos)
q = elegir_primo(primos)

while p == q:  # Asegura que P y Q sean diferentes
    q = elegir_primo(primos)

print(f"P: {p}, Q: {q}")

# Paso 2: Calcular N = P * Q
n = p * q
print(f"N (P * Q): {n}")

# Paso 3: Calcular pi(n) = (P-1) * (Q-1)
pi_n = (p - 1) * (q - 1)
print(f"Pi(n): {pi_n}")

# Paso 4: Elegir 'e' que cumpla con 1 < e < pi(n) y mcd(e, pi(n)) = 1
e = elegir_primo(primos, pi_n)  # Selecciona 'e' que cumple con la condición
print(f"E: {e}. Es mayor a 1 y menos a Pi(n): {1 < e < pi_n}")

# Paso 5: Generar llave pública (e, n)
llave_publica = (e, n)
print(f"Llave pública: (E: {llave_publica[0]}, N: {llave_publica[1]})")

# Paso 6: Calcular 'd' para la llave privada utilizando congruencia lineal
d = calcular_d(e, pi_n)
llave_privada = (d, n)
print(f"Llave privada: (D: {llave_privada[0]}, N: {llave_privada[1]})")

# Resultados finales
print(f"Generación de Llaves RSA completada.")
print(f"Llave Pública: (e={llave_publica[0]}, n={llave_publica[1]})")
print(f"Llave Privada: (d={llave_privada[0]}, n={llave_privada[1]})")
