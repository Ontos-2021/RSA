# Acá estará el main

""" Paso 1
Primero, hay que elegir dós números primos aleatorios
En este caso, P y Q

P = 83
Q = 97 """
import MCD.MCD

""" Paso 2
Una vez que tenemos P y Q, podemos determinar N.
La ecuación es N = P * Q

N = P * Q = (83) * (97) = 8051 """

""" Paso 3
Luego hay que determinar pi(n).
El cual es
pi(n) = (p-1)(q-1) = (83-1)(97-1) = (82)(96) = 7872 """

""" Paso 4
Luego hay que encontrar o elegir 'e'.
El cual tiene dos condiciones
1 < e < pi(n) y e = int | En un tutorial decía que era '1 < e'.
mcd(e, pi(n))= = 1 """

""" Llave pública = (e, n)
    Llave privada = (d, n)
"""

from PRIMOS.primos import *
from MCD.MCD import *
from random import randint as random

# Paso 1 | Crear P y Q

primos = crear_primos()

p = primos[random(int((len(primos) / 2)), len(primos))]

# Hay que asegurarse de que p y q nunca sean iguales
q = primos[random(int((len(primos) / 2)), len(primos))]

print(f"P: {p} Q: {q}")

mcd = mcd(p, q)

# Paso 2 | Determinar N | N = P * Q

n = p * q
print(f"Factores de N: {factorizar(n)}")

print(f"N: {n}")

# Paso 3 | Determinar pi(n) | pi(n) = (P-1) * (Q-1)

pi_n = (p - 1) * (q - 1)

print(f"Pi(n): {pi_n}")

# Paso 4 |
""" Paso 4
Luego hay que encontrar o elegir 'e'.
El cual tiene dos condiciones
1 < e < pi(n) y e = int | En un tutorial decía que era '1 < e'.
mcd(e, pi(n))= = 1 """

e = primos[random(int((len(primos) / 2)), len(primos))]

print(f"E: {e}. Es mayor a 1 y menos a Pi(n): {1 < e < pi_n}")
print(f"Máximo común divisor: {MCD.MCD.mcd(e, pi_n)}")
