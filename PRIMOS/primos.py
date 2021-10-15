# Acá irán las funciones relacionadas a números primos

def crear_primos():
    primos = [2]
    n = 3
    for i in range(1, 100000):

        # Verificar si n es divisible por alguno de los primos ya encontrados

        es_primo = True

        for primo in primos:

            # En este caso n no es divisible por el primo actual
            if n % primo == 0:

                es_primo = False
                # print(f"n: {n}, primo = {es_primo}. Número primo por el cual se divide: {primo}")
                break

            # rint(f"n: {n}, primo = {es_primo}. Número primo por el cual se divide: {primo}")

        if es_primo:

            primos.append(n)

        n += 2

    print(f"Estos son los números primos: {primos}")

