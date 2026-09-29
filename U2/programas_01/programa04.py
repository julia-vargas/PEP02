# #programa04
# #Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
# #nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
# #cuenta los siguientes rangos:
#   Insuficiente: [0, 5)
#   Suficiente: [5, 6)
#   Bien: [6, 7)
#   Notable: [7, 9)
#   Sobresaliente: [9, 10]
# Programación en Python (PEP) - IES Leonardo Da Vinci - Álvaro García
# U2P02-Programas_01. Estructuras condicionales
# Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un
# mensaje de error indicando que la nota no es válida.
# Hay que usar la estructura match.

num = int(input("Introduzca la nota:"))

match num:
    case 0 | 1 | 2 | 3 | 4:  # En lugar de hacer 80 case, puedo separarlo con pipelines
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6:
        print("Bien")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:
        print("La nota no es válida")
