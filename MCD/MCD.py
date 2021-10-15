# Acá se calculará el mínimo común múltiplo entre dos números

def mcd(a, b):
    divisores_a = factorizar(a)

    divisores_b = factorizar(b)

    divisores_comunes = []

    for i in divisores_a:
        for j in divisores_b:
            if i == j:
                divisores_comunes.append(i)
                divisores_b.remove(i)
                break

    # print(f"Divisores comunes: {divisores_comunes}")
    maximo_comun_divisor = 1
    for divisor in divisores_comunes:
        maximo_comun_divisor = maximo_comun_divisor * divisor

    return maximo_comun_divisor


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

    # print(f"Estos son los divisores de {numero_inicial}: {divisores}")
    return divisores
