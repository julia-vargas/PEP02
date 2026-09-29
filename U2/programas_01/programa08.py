# programa08
# Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
# saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
# sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
# Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
# random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
# debes poner import random al inicio del programa)

import random

d1 = random.randrange(1, 7)  # Ya me devuelve un int así que no hago cast
d2 = random.randrange(1, 7)
d3 = random.randrange(1, 7)
d4 = random.randrange(1, 7)

jugador1 = d1 + d2
jugador2 = d3 + d4
if jugador1 > jugador2:
    print("Ha ganado el primer jugador")
elif jugador1 < jugador2:
    print("Ha ganado el segundo jugador")
else:
    # primero averiguamos la tirada más alta del primero
    if d1 < d2:
        alto1 = d2
    else:
        alto1 = d1

    # ahora la del segundo
    if d3 < d4:
        alto2 = d4
    else:
        alto2 = d3

    # y luego lo comparamos
    if alto1 < alto2:
        print("Ha ganado el segundo jugador")
    elif alto1 > alto2:
        print("Ha ganado el primer jugador")
    else:
        print("Han empatado")
