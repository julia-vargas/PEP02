# programa08
# Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
# solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
# respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
# termina cuando se acierta el número.
# Puedes generar el número usando la función random.randrange(1, 21) para
# obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
# del programa).
# Mejora el programa de forma que el usuario tenga solo 3 intentos.

import random

num_ganador = random.randrange(1, 21) 
num_adivinado = 0

while num_adivinado != num_ganador:
    num_adivinado = int(input("Introduzca el numero a adivinar"))
    if num_adivinado < num_ganador:
        print("El numero a adivinar es mayor")
    elif num_adivinado > num_ganador:
        print("El numero a adivinar es menor")
    else:
        print("Has acertado!")
        

#La versión mejorada:

num_ganador = random.randrange(1, 21) 
num_adivinado = 0
intentos = 0

while num_adivinado != num_ganador and intentos != 3:
    num_adivinado = int(input("Introduzca el numero a adivinar"))
    if num_adivinado < num_ganador:
        print("El numero a adivinar es mayor")
        intentos = intentos + 1
    elif num_adivinado > num_ganador:
        print("El numero a adivinar es menor")
        intentos = intentos + 1
    else:
        print("Has acertado!")
        
if intentos == 3:
    print("Te has quedado sin intentos")