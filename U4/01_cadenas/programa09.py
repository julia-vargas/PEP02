# Programa09: Unicode y ASCII
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Muestra el código Unicode de un emoji (ord(), hex()).
#  Crea un carácter a partir de un código numérico (chr()).
#  Imprime los caracteres ASCII del 48 al 57 (dígitos) en una línea.


print("😊:", ord("😊")) # ordinal
print("😊 en hexadecimal:", hex(ord("😊"))) # hexadecimal

for i in range(48, 58):
    print(chr(i))
print()