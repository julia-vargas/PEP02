# programa02
# Modifica el programa principal (main,py) del ejercicio anterior para que siga la siguiente
# estructura


# imports de la librería estándar (no hay)
# imports de librerías de terceros (no hay)
# imports de módulos propios
import operaciones
# Definición de funciones principales
def main():
    """Función principal del programa"""
    print("Hola, este es el programa principal")
    n1 = int(input("Introduzca el primer número: "))
    n2 = int(input("Introduzca el segundo número: "))

    print(operaciones.suma(n1, n2))
    print(operaciones.resta(n1, n2))
    print(operaciones.multiplicacion(n1, n2))
    print(operaciones.division(n1, n2))

# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()

