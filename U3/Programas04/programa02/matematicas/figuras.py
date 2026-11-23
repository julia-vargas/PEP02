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

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_triangulo(base, altura):
    area = base * altura / 2
    return area

def area_circulo(radio):
    area = 3.14 * radio * radio
    return area

