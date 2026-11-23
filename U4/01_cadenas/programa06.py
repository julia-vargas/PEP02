# Programa06: Slicing e iteración
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Crea una cadena "Python".
#  Extrae la subcadena "Pyt" con slicing.
#  Extrae los caracteres en posiciones pares con slicing ::2.
#  Invierte la cadena con slicing [::-1].
#  Recorre la cadena carácter por carácter e imprímelos.

cadena = "Python"
subcadena = cadena [0:3]
pares = cadena[::2]
inversa = cadena[::-1]

print("Cadena original:", cadena)
print("Subcadena 'Pyt':", subcadena)
print("Caracteres en posiciones pares:", pares)
print("Cadena invertida:", inversa)

for caracter in cadena:
    print(caracter)