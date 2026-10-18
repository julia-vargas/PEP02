# programa04
# Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
# valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
# que pida muestre un aviso y vuelva a pedir el valor.

def calcular_area_circulo(radio):
    area = radio * radio * 3.14
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def opcion1():
    while True:
        radio = float(input("Introduzca el radio del círculo"))
        if radio > 0:
            resultado = calcular_area_circulo(radio)
            return resultado
        else:
            print("El radio debe ser mayor de 0")

def opcion2():
    while True:
        base = float(input("Introduzca la base del triángulo"))
        altura = float(input("Introduzca la altura del triángulo"))
        if base > 0 and altura > 0:
            resultado = calcular_area_triangulo(base, altura)
            return resultado
        else:
            print("La base y la altura deben ser mayores de 0")

def opcion3():
    while True:
        base = float(input("Introduzca la base del rectángulo"))
        altura = float(input("Introduzca la altura del rectángulo"))
        if base > 0 and altura > 0:
            resultado = calcular_area_rectangulo(base, altura)
            return resultado
        else:
            print("La base y la altura deben ser mayores de 0")

def main():
    while True:
        mostrar_menu()
        opc = int(input("Introduce una opción (1-4): "))
        match opc:
            case 1:
                resultado = opcion1()
                print("El resultado es", resultado)
            case 2:
                resultado = opcion2()
                print("El resultado es", resultado)
            case 3:
                resultado = opcion3()
                print("El resultado es", resultado)
            case 4:
                print("Fin")
                break
            case _:
                print("Introduzca una opción válida")

main()