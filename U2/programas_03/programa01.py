# programa01
# Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
# pedir el número hasta que no se introduzca correctamente. Controla las posibles
# excepciones a la hora de introducir el número por teclado.

num = 0

while num < 1 or num > 10:
    try:
        num = int(input("Introduzca un número del 1 al 10"))
    except Exception as ex:
        print("Error, intriduzca un número válido")
        
