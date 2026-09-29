# programa05
# Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
# o que indique que son iguales

n1 = int(input("Introduzca el primer numero:"))
n2 = int(input("Introduzca el segundo numero:"))

if n2 < n1:
    print("El primero es mayor")
elif n2 > n1:
    print("El segundo es mayor")
else:
    print("Son iguales")
