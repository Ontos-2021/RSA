# Acá estará el main

""" Paso 1
Primero, hay que elegir dós números primos aleatorios
En este caso, P y Q

P = 83
Q = 97 """

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
1 < e < pi(n) | En un tutorial decía que era '1 < e'.
mcd(e, pi(n))= = 1 """

""" Llave pública = (e, n)
    Llave privada = (d, n)
"""

from PRIMOS.primos import *
from MCD.MCD import *
from random import randint as random

# Paso 1 | Crear P y Q

primos = crear_primos()
print(f"Random: {int((len(primos) / 2)), len(primos)}")
p = primos[random(int((len(primos) / 2)), len(primos))]

# Hay que asegurarse de que p y q nunca sean iguales
q = primos[random(int((len(primos) / 2)), len(primos))]

print(f"P: {p} Q: {q}")

mcd = mcd(p, q)

print(f"Máximo común múltiplo entre {p} y {q}: {mcd}")
