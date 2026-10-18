# programa05
# Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
# en Python (globales, no locales y locales).

#VARIABLE LOCAL
def mostrar():
    a = 2
    print(a)

mostrar()
print(a) # Error, la variable local a solo es "visibe/existe"
#dentro de la funcion.

#VARIABLE GLOBAL
def mostrar():
    global a #para que python sepa que es la a de fuera
    print(a) #escribe 5, que es lo que vale a
    a = 1 #modifica el a de fuera
    return

a = 5
mostrar()
print(a)


#VARIABLE NO LOCAL
def funcion_exterior():
    mensaje = "Hola"  # Variable no local para la función interna
    
    def funcion_interior():
        nonlocal mensaje #para que python la considere local
        mensaje = "Hola2" #sobreescribimos mensaje
        print(mensaje) #me devuelve hola2
        
    funcion_interior()
    print(mensaje) #me devuelve hola

funcion_exterior()
