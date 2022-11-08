'''escribe un programa para abrir el archivo romeo.txt y leer
linea a linea. Para cada linea, dividir la linea en una
lista de palabras utilizando la funcion split para
cada palabra, revisar si la palabra ya se encuentra previamente 
en la lista, si la palabra no esta en la lista entonces
agregarla cuando el programa termine ordene en escribir las palabras
resultantes en orden alfabetico'''

efe = []

def jeje(b):
    for c in b:
        if not c in efe:
            efe.append(c)

def jaja(a):
    return a.split()

def hola(manejador):

    for linea in manejador:
        jeje(jaja(linea))

hola(open("actividad7/romeo.txt"))
efe.sort()

print(efe)
