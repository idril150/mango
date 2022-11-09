'''Escribe un programa para leer a través de un historial de correos, 
construye un histograma utilizando un diccionario para contar 
cuantos mensajes han llegado de cada dirección de correo electrónico, 
e imprime el diccionario'''

d = dict()

def separador(a):
    b = a.split()
    return b[1]

def hola(manejador):

    for linea in manejador:
        if len(linea.split()) == 0 or linea.split()[0] != 'From':
           
            continue
        d[separador(linea)] = d.get(separador(linea),0)+1
        


hola(open("actividad7/mbox-short.txt"))
print(d)