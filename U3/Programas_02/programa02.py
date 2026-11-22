# programa02
# Modifica el programa anterior para que solo se importen las funciones del módulo math
# que se usan en el programa.

import math.sin
import math.radians
import math.sqrt
import math.cos
import math.pow


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
