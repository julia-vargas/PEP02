# programa04
# El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
# de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
# por defecto en el interprete de Python.
# Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
# escribe un programa que:
#  Dibuje un cuadrado rojo sin rellenar.
#  Dibuje un circulo verde relleno.

import turtle

pantalla = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.color("red")
for _ in range(4):
    tortuga.forward(100)
    tortuga.left(90)

tortuga.forward(200)

tortuga.color("green")
tortuga.fillcolor("green")
tortuga.begin_fill()
tortuga.circle(50)  
tortuga.end_fill()

tortuga.hideturtle()
pantalla.exitonclick()