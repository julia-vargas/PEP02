# programa09
# Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
# lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
# continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
# para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
# puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
# banca gana.

import random

baza_ordenador = random.randrange(17, 22)  # Ya me devuelve un int así que no hago cast
baza_jugador = random.randrange(1, 6)
sacar_carta = ""  # Lo incializo a cualqioer cosa menos un si o un no
print("Numero jugador: ", baza_jugador)


while sacar_carta != "no":  # Hasta que no quiera dejar de sacar cartas, no para
    sacar_carta = input("Desea sacar otra carta más?: (si, no)")
    if sacar_carta == "si":
        baza_jugador = baza_jugador + random.randrange(1, 6)
        print("Numero jugador: ", baza_jugador)

if (baza_jugador > 21) or (
    baza_jugador <= baza_ordenador
):  # Si tiene mas de 21 o tiene igual o menos que el ordenador, peride
    print("El jugador ha perdido")
else:
    print("El jugador ha ganado")

print("Numero ordenador: ", baza_ordenador)
