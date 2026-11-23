from random import randint

# FUNCIONES:


def calcular_energia(fuerza, conocimiento):
    try:
        energia = fuerza + conocimiento + randint(1, 3)  # VER SI ME LOS COGE
        return energia
    except ValueError:
        print("Debes introducir números")


def calcular_puntos(valor_tesoro, bonus):
    puntos = valor_tesoro + bonus
    return puntos


def mostrar_explorador(nombre, energia, puntos):
    print("Nombre del explorador: ", nombre)
    print("Energía del explorador: ", energia)
    print("Puntos del explorador: ", puntos)
