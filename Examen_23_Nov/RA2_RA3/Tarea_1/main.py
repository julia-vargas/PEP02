# imports de la librería estándar, ninguno
# imports de librerías de terceros, ninguno
# imports de módulos propios
from exploracion import explorador, isla

# excepcoion  1, que no pueda meter otro valor que no sea los que se piden para el enunciado


# Definición de funciones principales
def main():
    print("\n=== EXPLORADORES DEL TESORO ===")
    nombre = input(
        "Nombre del explorador: "
    )  # no hace falta convertirlo (input es string)
    fuerza = int(input("fuerza (1-10): "))
    conocimiento = int(input("Conocimiento (1-5): "))

    # Calculamos su energía, y sus puntos parten de 0
    energia = explorador.calcular_energia(fuerza, conocimiento)
    energia_inicial = energia  # nos guardamos el valor de la energia inicial
    puntos = 0

    # MOSTRAMOS AL EXPLORADOR
    explorador.mostrar_explorador(nombre, energia, puntos)

    for jornada in range(4):
        print("\n --- JORNADA", jornada, "---")

        if (
            energia == 0
        ):  # Si la energía es 0 al inicio de la jornada, descansa obligatriamente y pasa a la siguiente iteración del bucle
            print("¡Has encontrado unlugar de descanso!")
            energia = energia + 2
            if energia > energia_inicial:
                energia = energia_inicial  # así nunca superará la energía inicial
            continue

        evento = isla.generar_evento(energia)  # Generamos el evento

        match evento:  # dependiendo del evento hará una cosa u otra
            case 1:  # TESORO
                print("¡Has encontrado un tesoro!")

                # calculamos el valor del tesoro
                valor_tesoro = isla.valor_tesoro(energia)

                # calculamos el bonus para los puntos
                bonus = 0  # parte de 0, y si no es mayor o igual a 10, se queda en 0
                if energia >= 10:
                    bonus = 5
                print("Bonificación: ", bonus)

                puntos_jornada = explorador.calcular_puntos(valor_tesoro, bonus)

                print("Puntos obtenidos: ", puntos_jornada)

                puntos = puntos + puntos_jornada

            case 2:  # TRAMPA
                print("¡Has caído en una trampa!")
                print("Pierdes 2 puntos de energía")
                energia = energia - 2
                if (  # noqa: PLR1730
                    energia < 0
                ):  # Si la energía ha acabado con menos de 0, la reseteamos a 0 para no tener menos de 0
                    energia = 0

            case 3:  # DESCANSO
                print("¡Has encontrado unlugar de descanso!")
                print("Recuperas 2 puntos de energía")
                energia = energia + 2

        print("Energía: ", energia)
        print("Puntos acumulados: ", puntos)

    print("\n=== FIN DE LA EXPEDICIÓN ===")
    # MOSTRAMOS AL EXPLORADOR
    explorador.mostrar_explorador(nombre, energia, puntos)

    if puntos >= 30:
        print("¡Explorador legendario!")
    elif 15 <= puntos <= 29:
        print("¡Buena expedición!")
    else:
        print("¡Sigue explorando!")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
