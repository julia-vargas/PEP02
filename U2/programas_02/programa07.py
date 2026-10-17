# programa07
# Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
# suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
# la instrucción break y otra no.

suma = 0
numeros = 0
num = 1

while num != 0:
    num = int(input("Introduzca un numero"))
    if num != 0:
        numeros = numeros + 1
        suma = suma + num
        
print("La suma es: " , suma)
print("La media es: " , suma/numeros)


suma = 0
numeros = 0
num = 1

while True:
    num = int(input("Introduzca un numero"))
    if num == 0:
        break
    numeros = numeros + 1
    suma = suma + num
        
print("La suma es: " , suma)
print("La media es: " , suma/numeros)