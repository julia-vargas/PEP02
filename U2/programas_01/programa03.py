# programa03
# Escribe un programa que pida dos numero y muestre su división. Se deben tener en
# cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.

n1 = int(input("Introduzca el primer numero:"))
n2 = int(input("Introduzca el segundo numero:"))

if n2 != 0:
    print("Su división es: ", n1 / n2)
else:
    print("No se puede dividor entre 0")
