# programa03
# Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
# ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
# continue.

for i in range (0, 10, 2):
    print(i)
    
for i in range (0, 10):
    if i%2:
        continue
    print(i)
    
i=0
while i < 10:
    print(i)
    i = i + 2
    
i=0
print(i)
while i < 10:
    i = i + 1
    if i%2:
        continue
    print(i)
    