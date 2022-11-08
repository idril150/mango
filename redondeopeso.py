
def totala(a):
    return (round((a+(a*.16))))


def chicles():
    return (int(input("introduce la cantidad de chilces: "))*0.80)


def cerillito():
    return (int(input("introduce la cantidad de cerillitos: "))*1.26)


def jabon():
    return (int(input("introduce la cantidad de jabones: "))*18.45)


print("introduce tus cantidades compradas")


def suma(c, ce, ja):
    return (c+ce+ja)


print("el precio total es:", totala(suma(chicles(), cerillito(), jabon())))
