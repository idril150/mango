'''Escribe un programa que pide un alista de numeros e imprima 
el minimmo y macimo de esos numeros. solo despues de que 
el usuario escribe hecho'''
efe = []

def holiwi():
    a = int(input("introduce un numero: "))
    efe.append(a)

    while a != "hecho":
        a = input("introduce un numero: ")

        while True:

            try:
                b = int(a)
                efe.append(b)
                break

            except ValueError:            
                break

    return efe

print(holiwi())
print('el maximo es: ', max(efe))
print('el minimo es: ',min(efe))
