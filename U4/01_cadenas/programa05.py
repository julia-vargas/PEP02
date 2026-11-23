# Programa05: Operaciones básicas
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Declara dos cadenas y únelas con concatenación (+).
#  Repite una cadena tres veces con *.
#  Compara dos cadenas lexicográficamente e indica cuál es mayor.
#  Comprueba si una subcadena pertenece a otra con in.

cadena1 = "Hola"
cadena2 = "Adios"
cadena_concatenada = cadena1 + " " + cadena2
cadena_repetida = cadena1 * 3

print("Cadena concatenada:", cadena_concatenada)
print("Cadena repetida:", cadena_repetida)

if cadena1 > cadena2: # Se comparan por orden alfabético
    print(f"{cadena1} es mayor que {cadena2}")
else:
    print(f"{cadena2} es mayor que {cadena1}")

subcadena = "la"
if subcadena in cadena1:
    print(f'"{subcadena}" pertenece a "{cadena1}"') #Esta saltará, porque hola contiene "la"
if subcadena in cadena2:
    print(f'"{subcadena}" pertenece a "{cadena2}"')



