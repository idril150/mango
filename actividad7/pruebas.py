import string
d = dict()

def separador(a):
    
    
    return a.split()[2]

def hola(manejador):

    for linea in manejador:
        if len(linea.split()) == 0 or linea.split()[0] != 'Received:':
           
            continue
        #linea = linea.translate(linea.maketrans('','', string.punctuation))
        d[separador(linea)] = d.get(separador(linea),0)+1
        print (linea)


hola(open("actividad7/mbox-short.txt"))
#print(d)