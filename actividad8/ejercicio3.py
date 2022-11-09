d = dict()
def separador(a):
    b = a.split()
    return b[2]

def hola(manejador):

    for linea in manejador:
        if len(linea.split()) == 0 or linea.split()[0] != 'Received:':
           
            continue
        d[separador(linea)] = d.get(separador(linea),0)+1
        #print (linea)


hola(open("actividad7/mbox-short.txt"))
print(d)