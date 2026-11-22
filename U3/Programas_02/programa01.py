# programa01
# Escribe un programa en Python que importe el modulo math completo y que le pregunte al
# usuario que operación matemática quiere hacer:
# 1. Seno de un ángulo
# 2. Coseno de ángulo
# 3. Raíz cuadrada de un número
# 4. Potencia de dos números.
# Le pida los datos necesarios y muestre los resultados por pantalla.

import math

opc = 0
while opc != 5:
    print("\n***MENU***")
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")
    print("5. Salir")
    opc = int(input("¿Qué operación desea hacer? "))

    if opc == 1:
        angulo = float(input("Ingresa el ángulo en grados: "))
        print(f"El seno es: {math.sin(math.radians(angulo)):.4f}")

    elif opc == 2:
        angulo = float(input("Ingresa el ángulo en grados: "))
        print(f"El coseno es: {math.cos(math.radians(angulo)):.4f}")

    elif opc == 3:
        num = float(input("Ingresa un número: "))
        if num >= 0:
            print(f"La raíz cuadrada es: {math.sqrt(num):.4f}")
        else:
            print("No se puede calcular la raíz de un número negativo.")

    elif opc == 4:
        base = float(input("Ingresa la base: "))
        exponente = float(input("Ingresa el exponente: "))
        print(f"El resultado es: {math.pow(base, exponente)}")

    elif opc == 5:
        print("¡Hasta luego!")

    else:
        print("Opción no válida. Elige un número del 1 al 5.")




