# Programa08: Búsqueda y conteo
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Declara una cadena "programación en Python".
#  Busca la posición de "Python" con find() o index().
#  Cuenta cuántas veces aparece la letra "o".
#  Verifica si comienza por "pro" y termina por "on".

cadena = "programación en Python"
posicion = cadena.find("Python")
oes = cadena.count("o")
comienza = cadena.startswith("pro")
termina = cadena.endswith("on")

print("Posición de 'Python':", posicion)
print("Conteo de 'o':", oes)
print("Comienza por 'pro':", comienza) #Nos devuelven o true o false
print("Termina por 'on':", termina)