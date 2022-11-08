def divisible(t, n):
    return (t % n == 0)


def bisiesto(a):
    return (divisible(a, 4) and (not (divisible(a, 100)) or divisible(a, 400)))


def febrero28():
    return 28


def febrero29():
    return 29


def meses(a):
    def z():
        if (bisiesto(a)):
            return febrero29()
        else:
            return febrero28()

    return ([31, z(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])


def take(mes, a):
    return (meses(a)[:mes])


def numeroDia(d, m, a):
    return (((a-1) * 365
             + (a-1)//4
             - (a-1)//100
             + (a-1)//400
             + sum(take(m-1, a))
             + d
             ) % 7)


def d():
    return int(input(" Dia: "))


def m():
    return int(input(" Mes: "))


def a():
    return int(input(" Año: "))


def diasem(x):
    if (x) == 0:
        print("el dia es: 'Domingo'")
    elif x == 1:
        print("el dia es: 'Lunes'")
    elif x == 2:
        print("el dia es: 'Martes'")
    elif x == 3:
        print("el dia es: 'Miercoles'")
    elif x == 4:
        print("el dia es: 'Jueves'")
    elif x == 5:
        print("el dia es: 'Viernes'")
    else:
        print("el dia es: 'Sabado'")


print("Introduce la fecha")
diasem(numeroDia(d(), m(), a()))
