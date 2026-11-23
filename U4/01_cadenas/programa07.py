# Programa07: Métodos de cadena
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Declara una cadena " Hola Mundo ".
#  Aplica y muestra los resultados de: upper(), lower(), capitalize(),
# title().
#  Elimina espacios con strip().
#  Sustituye "Mundo" por "Python" con replace().
#  Divide la cadena en palabras con split().
#  Une una lista de palabras con join().

cadena = " Hola Mundo "
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())
print(cadena.strip())
print(cadena.replace("Mundo", "Python"))
print(cadena.split())
print(" ".join(["Hola", "Mundo"]))