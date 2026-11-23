# Programa03: Formato con str.format y f-strings
# Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#  Declara variables con tu nombre, curso y año.
#  Muestra un mensaje con str.format().
#  Muestra el mismo mensaje usando f-strings.
#  Usa un f-string para mostrar el resultado de una operación matemática con dos
# números.

nombre = "Julia"
curso = "Python"
anno = 2026

print("Nombre {}, curso {}, año {}".format(nombre, curso, anno))
print(f"Nombre {nombre}, curso {curso}, año {anno}")
print(f"2 * 6 = {2 * 6}")
