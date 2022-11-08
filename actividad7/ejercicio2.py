'''reescribe el codigo guardian de la diapositiva anterior sin las 2 sentencias
y. en vez de eso utiliza una expresion logica compuesta utilizando
el operador logico for con una sola sentencia if'''

def hola(manejador):

    for linea in manejador:
        if len(linea.split()) == 0 or linea.split()[0] != 'From':
            continue
        print(linea.split()[2])


hola(open("actividad7/mbox-short.txt"))
