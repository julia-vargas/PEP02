# programa02
# Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
# es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
# negativo) y si el valor no es correcto, mostrará un aviso.

num_par = int(input("Introdzca un número par"))

if num_par % 2 == 0:
    num_impar = int(input("Introdzca un número impar: "))

    if num_impar % 2 != 0:
        print("Todo OK")
    else:
        print("El segundo número no es impar")
else:
    print("El primer número no es par")
