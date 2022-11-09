'''Escribir un programa que clasifica cada mensaje de correo
dependiendo del día de la semana en que se recibió. 
Para hacer esto busca las líneas que comienzan con ‘From’, 
después busca por la tercer palabra y manten un contador para 
cada uno de los días de la semana. Al final del programa los contenidos 
del diccionario (el orden no importa).
'''
d = dict()
def separador(a):
    b = a.split()
    return b[2]

def hola(manejador):

    for linea in manejador:
        if len(linea.split()) == 0 or linea.split()[0] != 'From':
           
            continue
        d[separador(linea)] = d.get(separador(linea),0)+1
        


hola(open("actividad7/mbox-short.txt"))
print(d)