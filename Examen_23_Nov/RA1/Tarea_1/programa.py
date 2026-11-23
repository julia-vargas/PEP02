kilometros = float(input("Introduce los kilómetros recorridos: "))  # decimal
nombre = input(
    "Introduce el nombre del conductor: "
)  # string, no hace falta convertirlo porque todo input es string
num_ocupantes = int(input("Introduce el número de ocupantes del vehículo: "))  # entero

# IM^RIMIT LOS TIPOS DE LAS VARIABLES
print(type(kilometros))
print(type(nombre))
print(type(num_ocupantes))


# Comprobar que son del tipo correcto, almacenarlo en variables booleanas y mostrar que las 3 son true
es_decimal = isinstance(kilometros, float)  # True
es_string = isinstance(nombre, str)  # True
es_entero = isinstance(kilometros, int)  # True

print(es_decimal == True)
print(es_string == True)
print(es_entero == True)
# Todas devolverán True, porque true == true es true


# Constantes:
CONSUMO_100KM = 6.5
PRECIO_LITRO = 1.60
DESCUENTO = 0.10  # APLICARSELO AL COSTE TOTAL

litros = CONSUMO_100KM * kilometros / 100
coste = litros * PRECIO_LITRO
descuento = DESCUENTO * coste

print("---RESUMEN DEL VIAJE:---")
print("Número de kilómetros: ", kilometros)
print("Nombre del conductor: ", nombre)
print("Número de ocupantes: ", num_ocupantes)


print("Litros consumidos: ", litros, "litros")
print("Coste inicial: ", round(coste, 2), " euros")  # REDONDEADO A 2 DECIMALES
print(
    "Desscuento aplicado (10%): ", round(descuento, 2), " euros"
)  # REDONDEADO A 2 DECIMALES
print(
    "Coste final: ", round((coste - descuento), 2), " euros"
)  # REDONDEADO A 2 DECIMALES
print(
    "Importe por ocupante ", round((coste - descuento) / num_ocupantes, 2), " euros"
)  # REDONDEADO A 2 DECIMALES
