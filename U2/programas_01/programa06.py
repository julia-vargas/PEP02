# programa06
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta

dia = int(input("Introduzca el dia"))
mes = int(input("Introduzca el mes"))
anio = int(input("Introduzca el año"))

# Todas parten de ser falsas. No hace falta mes porque de eso se encarga el match (El día nunca será True)
dia_correcto = False


match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        if (dia <= 31) and (dia > 0):
            dia_correcto = True  # Si los días están bien, cambia a true
    case 2:
        if (dia <= 28) and (dia > 0):
            dia_correcto = True  # Si los días están bien, cambia a true
    case 4 | 6 | 9 | 11:
        if (dia <= 30) and (dia > 0):
            dia_correcto = True  # Si los días están bien, cambia a true

if dia_correcto == True:
    print("La fecha es correcta")
else:
    print("La fecha está mal")
