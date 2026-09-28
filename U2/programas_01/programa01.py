# programa01
# Escribe un programa que pida primero un número par y luego un número impar (positivos
# o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
# impar respectivamente), se mostrará un aviso.

num1 = int(input("Introdzcauce un número par: "))
es_par = num1 % 2 == 0

num2 = int(input("Introduce un número impar: "))
es_impar = num2 % 2 != 0

if es_par and es_impar:
    print("Todo OK")
else:
    if not es_par:
        print("El primer número no es un número par")
    if not es_impar:
        print("El segundo número no es un número impar")
