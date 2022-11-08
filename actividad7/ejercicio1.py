'''escribe una funcion llamada recortar que toma una lista y la modifica 
removiendo el primer y ultimo elemento y regresa none
despues escriba una funcion llamada medio que toma en una lista y regresa una nueva 
lista que contiene todo excepto el primer y ultimo elemento de la lista'''

def recortar(a):
    del a[1:-1]


def medio(t):
    return t[1:-1], recortar(t)


print(medio(input("\nintroduce la lista separado por comas\n").split(',')))
