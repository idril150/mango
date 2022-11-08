manejador = open("actividad7/mbox-short.txt")
contador = 0
for linea in manejador:
    palabras = linea.split()

    if len(palabras) == 0 or palabras[0] != 'From' :continue
    print(palabras[2])
