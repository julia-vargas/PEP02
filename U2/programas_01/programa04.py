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

if (num >= 0) and (num <= 10):
    print("Su división es: ", n1 / n2)
else:
    print("No se puede dividor entre 0")
