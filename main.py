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

p = primos[random(int((len(primos) / 2)), len(primos) - 1)]

# Hay que asegurarse de que p y q nunca sean iguales
q = primos[random(int((len(primos) / 2)), len(primos) - 1)]
# p = 83
# q = 97
print(f"P: {p} Q: {q}")

mcd = mcd(p, q)

# Paso 2 | Determinar N | N = P * Q

n = p * q

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

e = primos[random(int((len(primos) / 2)), len(primos) - 1)]

print(f"E: {e}. Es mayor a 1 y menos a Pi(n): {1 < e < pi_n}")
print(f"Máximo común divisor entre E y Pi(n): {MCD.MCD.mcd(e, pi_n)}")

# Paso 5 | Crear llave pública | Llave pública = (e, n)

llave_publica = (e, n)

print(f"Llave pública: (E: {llave_publica[0]}, N: {llave_publica[1]})")

# Paso 6 | Determinar la llave privada | Se determina por Congruencia Lineal

""" 
E * D = 1 ( mod Pi(n))

-> E * D = 1 + K (P - 1) * (Q - 1)

-> Fórmula: D = (1 + K * Pi(n))/ E

Al parecer D tiene que ser un número entero

K es un número entero y K >= 1.
"""


def calcular_d(k, pi_n, e):
    d = (1 + (k * pi_n)) / e
    return d


d_posibles = []
for k in range(2, 10):
    d = calcular_d(k, pi_n, e)
    if d % 1 == 0:
        d_posibles.append([d, k])

llave_privada = (d_posibles[random(0, (len(d_posibles) - 1))], n)

print(f"Llave privada: (D: {int(llave_privada[0][0])}, N: {llave_privada[1]})")

print(f"K: {llave_privada[0][1]}")

# Encriptar | Ci = Mi ^ E (mod n)
mi = 5

print(f"Mi: {mi}")
ci = (mi ** llave_publica[0]) % llave_publica[1]
print(f"Ci: {ci}")

# Descencriptar | Mi = Ci ^ D (mod n)
print(f"D: {(int(llave_privada[0][0]))}, N: {llave_privada[1]}")


mensaje_descencriptado = (ci ** llave_privada[0][0]) % llave_privada[1]

print(f"El mensaje descencriptado es: {mensaje_descencriptado}")
