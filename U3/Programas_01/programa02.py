# programa02
# Escribe un programa en Python que haga uso de una función llamada saludar que cumpla
# los siguientes requisitos:
#  Entrada: Tiene 4 parámetros de entrada, que serán 4 cadenas de texto: nombre,
# primer apellido, segundo apellido y curso. El parámetro curso tendrá en la
# declaración de la función el valor por defecto “2DAW”
#  Salida: No tiene parámetros de salida.
#  Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se
# haya pasado como parámetro de entrada.
# El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar
# el paso de parámetros de forma nominal (con clave valor).

def saludar(nombre, primer_apellido, segundo_apellido, curso="2DAW"):
    print("Hola, " , nombre, primer_apellido, segundo_apellido, ", bienvenido a ", curso)

saludar("Julia", "Vargas", "de Pastors")
saludar(nombre="Julia", primer_apellido="Vargas", segundo_apellido="de Pastors")
nombre="Fulanito"
primer_apellido="de"
segundo_apellido="Tal"
saludar(nombre, primer_apellido, segundo_apellido)
