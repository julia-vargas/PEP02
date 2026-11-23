# programa01
# Crea un paquete llamado matemáticas que contenga tres módulos:
#  operaciones: creado en la práctica anterior.
#  figuras: tendrá las siguientes funciones.
# ◦ area_rectangulo(base, altura): devuelve el área.
# ◦ area_triangulo(base, altura): devuelve el área.
# ◦ area_circulo(radio): devuelve el área.
#  conversiones.py: tendrá las siguientes funciones
# ◦ a_binario(n): devuelve la representación binaria de un número entero en forma
# de cadena.
# ◦ a_hexadecimal(n): devuelve la representación hexadecimal de un número
# entero en forma de cadena.
# ◦ a_entero(texto): convierte una cadena numérica en un entero (controlando
# errores si el texto no es válido)
# Recuerda que debes incluir el fichero __init__.py aunque esté vacío.
# Crea un programa principal main.py que muestre un menú que permita elegir entre:
#  Operaciones matemáticas
#  Cálculo de áreas geométricas
# Según la opción elegida, pida al usuario los datos necesarios y muestre el resultado
# correspondiente

# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios
from matematicas import operaciones, figuras, conversiones


# Definición de funciones principales
def main():
    """Función principal del programa"""
    print("Hola, este es el programa principal")

    opc = ""
    while opc != "4":  # con texto potque el input es un string
        print("1. Operaciones matemáticas")
        print("2. Cálculo de áreas geométricas")
        print("3. Conversiones")
        print("4. Fin")
        opc = input("Introduzca la opción deseada: ")

        match opc:
            case "1":
                opc_1 = ""
                while opc_1 != "5":
                    a = float(input("Introduzca el primer número: "))
                    b = float(input("Introduzca el segundo número: "))

                    print("1. Suma")
                    print("2. Resta")
                    print("3. Multiplicación")
                    print("4. División")
                    print("5. Volver al menú principal")
                    opc_1 = input("Introduzca la opción que desea: ")

                    match opc_1:
                        case "1":
                            print("Resultado:", operaciones.suma(a, b))
                        case "2":
                            print("Resultado:", operaciones.resta(a, b))
                        case "3":
                            print("Resultado:", operaciones.multiplicacion(a, b))
                        case "4":
                            print("Resultado:", operaciones.division(a, b))
                        case "5":
                            print("Volviendo")
                        case _:
                            print("Opción no válida")

            case "2":
                opc_2 = ""
                while opc_2 != "4":
                    print("1. Área del rectángulo")
                    print("2. Área del triángulo")
                    print("3. Área del círculo")
                    print("4. Volver al menú principal")
                    opc_2 = input("Introduzca la opción ddeseada: ")

                    match opc_2:
                        case "1":
                            base = float(input("Introduzca la base: "))
                            altura = float(input("Introduzca la altura: "))
                            print(
                                "Área del rectángulo:",
                                figuras.area_rectangulo(base, altura),
                            )
                        case "2":
                            base = float(input("Introduzca la base: "))
                            altura = float(input("Introduzca la altura: "))
                            print(
                                "Área del triángulo:",
                                figuras.area_triangulo(base, altura),
                            )
                        case "3":
                            radio = float(input("Introduzca el radio: "))
                            print("Área del círculo:", figuras.area_circulo(radio))
                        case "4":
                            print("Volviendo")
                        case _:
                            print("Opción no válida")

            case "3":
                opc_3 = ""
                while opc_3 != "4":
                    print("1. Entero a binario")
                    print("2. Entero a hexadecimal")
                    print("3. Texto a entero")
                    print("4. Volver al menú principal")
                    opc_3 = input("Introduzca la opción que desea: ")

                    match opc_3:
                        case "1":
                            n = int(input("Introduzca un número entero: "))
                            print("En binario:", conversiones.a_binario(n))
                        case "2":
                            n = int(input("Introduzca un número entero: "))
                            print("En hexadecimal:", conversiones.a_hexadecimal(n))
                        case "3":
                            texto = input("Introduzca una cadena numérica: ")
                            print("Entero convertido:", conversiones.a_entero(texto))
                        case "4":
                            print("Volviendo")
                        case _:
                            print("Opción no válida")

            case "4":
                print("Fin")
            case _:
                print("Opción no válida")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
