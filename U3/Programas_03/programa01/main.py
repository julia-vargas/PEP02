# programa01
# Crea un módulo llamado operaciones que contenga cuatro funciones básicas
# relacionadas con operaciones numéricas:
#  suma(a, b) → devuelve la suma de dos números.
#  resta(a, b) → devuelve la resta de dos números.
#  multiplicacion(a, b) → devuelve la multiplicación de dos números.
#  division(a, b) → devuelve la división de dos números (controlando la división entre
# cero).
# Crea un programa principal main.py que y importe el módulo matemáticas, pida al usuario
# dos números y muestre los resultados de aplicar cada una de las funciones anteriores

import operaciones

n1 = int(input("Introduzca el primer número: "))
n2 = int(input("Introduzca el segundo número: "))

print(operaciones.suma(n1, n2))
print(operaciones.resta(n1, n2))
print(operaciones.multiplicacion(n1, n2))
print(operaciones.division(n1, n2))