# programa09
# Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
# lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
# qué opción desea elegir. Por ejemplo:
# 1. Piedra
# 2. Papel
# 3. Tijera
# Seleccione una opción (1, 2 o 3):
# Después de leer la opción seleccionada por el usuario el programa generará un número
# aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
# ganado o ha perdido dependiendo del resultado.
# Ten en cuenta que:
#  La piedra gana a la tijera pero pierde contra el papel.
#  El papel gana a la piedra pero pierde contra la tijera.
#  La tijera gana al papel pero pierde contra la piedra.

import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
jugador = int(input("Seleccione una opción (1, 2 o 3): "))

maquina = random.randrange(1, 4)

# Para ver si lo hace bien
print(jugador)
print(maquina)

if (jugador >= 1 and jugador <= 3):
    if jugador == maquina:
        print("Empate")
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        print("Ha ganado el jugador")
    else: # si no es ni empate ni victoria, pierde
        print("Ha ganado la maquina")
else:
    print("Opcion no valida. Reinicie el programa")