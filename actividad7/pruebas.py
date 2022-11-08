efe=[]


def holiwi():
    n1 = int(input("introduce un numero "))
    efe.append(n1)
    
    while n1 != "hecho":
        n1 = input("introduce un numero ")

        while True:

            try:
                n2 = int(n1)
                efe.append(n2)
                break
                
            except ValueError:
                break

    return efe


print(holiwi())
print(max(efe))
print(min(efe))




