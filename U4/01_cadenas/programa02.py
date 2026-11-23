# Programa02: Caracteres especiales y cadenas largas
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Crea una cadena que incluya saltos de línea y tabuladores usando \n y \t.
#  Divide una cadena larga en varias líneas sin perder legibilidad.
#  Muestra el resultado en pantalla

cadena_1 = "Primera línea\n\tSegunda línea tabulada\n\t\tTercera línea con doble tabulación"

# con paréntesis se unen automáticamente las cadenas sin insertar saltos de línea extra
cadena_2 = (
    "Esta es una cadena "
    "de texto muy larga "
    "que dividimos en varias líneas"
)

print("--- Caracteres especiales ---")
print(cadena_1)

print("\n--- Cadena larga ---")
print(cadena_2)
