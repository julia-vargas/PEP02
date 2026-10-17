# programa10
# Modifica el programa anterior par que pida en primer lugar el número de jugadores que
# van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
# banca.

import random

baza_ordenador = random.randrange(17, 22)  # Ya me devuelve un int así que no hago cast


jugadores = input("Cuántos jugadores van a jugar? (valor numérico)")

for jugador in (int)jugadores:






print("Numero jugador", i, ": ", baza_jugador)




baza_jugador = random.randrange(1, 6)
sacar_carta = ""  # Lo incializo a cualqioer cosa menos un si o un no

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
