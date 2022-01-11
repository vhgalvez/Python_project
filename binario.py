"""
    https://parzibyte.me/blog
"""
def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    # https://parzibyte.me/blog/2019/06/26/invertir-cadena-python/
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal


# Probar
binario = input("Ingresa un número binario: ")
decimal = binario_a_decimal(binario)
print(decimal)