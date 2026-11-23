from random import randint

# FUNCIOENS


def generar_evento(energia):
    num = randint(1, 5)  # numero aleatorio
    if energia < 10:
        match num:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 2
            case 4:
                return 3
            case 5:
                return 3
    else:  # si no es menor de 10, será igual o mayor
        match num:
            case 1:
                return 1
            case 2:
                return 1
            case 3:
                return 1
            case 4:
                return 2
            case 5:
                return 3


def valor_tesoro(energia):
    valor_tesoro = energia + randint(1, 5)
    return valor_tesoro
