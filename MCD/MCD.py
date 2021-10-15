# Acá se calculará el mínimo común múltiplo entre dos números

def mcd(a, b):
    # Todavía construyendo
    divisores_a = factorizar(a)

    divisores_b = factorizar(b)

    divisores_comunes = []

    for i in divisores_a:
        for j in divisores_b:
            if i == j:
                divisores_comunes.append(i)
                divisores_a.remove(i)
                divisores_b.remove(j)

    return divisores_comunes


def factorizar(numero):
    divisores = [1]

    numero_inicial = numero

    i = 2

    while i <= numero:

        if numero % i == 0:
            divisores.append(i)

            listo = False
            numero = numero / i
            while not listo:

                if numero % i == 0:
                    divisores.append(i)
                    numero = numero / i
                else:
                    listo = True

        producto = 1

        for divisor in divisores:
            producto = producto * divisor

        if producto >= numero_inicial:
            break

        i += 1
    print(f"Estos son los divisores de {numero_inicial}: {divisores}")
    return divisores


factorizar(123456)
