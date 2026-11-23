# Programa01: Creación, longitud y acceso Básico
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Define tres cadenas con comillas simples, dobles y triples.
#  Muestra en pantalla cada una.
#  Accede y muestra el primer y último carácter de una cadena mediante índices
# positivo y negativo.

cadena1 = 'Hola, mundo!'
cadena2 = "Hola, mundo!"
cadena3 = """Hola, mundo!"""

print("Cadena 1:", cadena1)
print("Cadena 2:", cadena2)
print("Cadena 3:", cadena3)

# como si fuese un array. Si el valor es negativo, empieza a contar desde el final de la cadena
print("Primer carácter de cadena1:", cadena1[0])
print("Último carácter de cadena1:", cadena1[-1]) 