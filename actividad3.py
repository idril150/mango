a =  int (input("tablas de que numero? "))
def tablas(x):    
    return x*a
num = [1,2,3,4,5,6,7,8,9,10]
print (list(map(tablas, num)))

# Prueba Para saber los dias

def divisible(t,n):
    return(t % n == 0)

def bisiesto(a):
    return (divisible(a,4) and (not(divisible(a, 100)) or divisible(a, 400)))

def febrero28():
    return 28

def febrero29():
    return 29

def arrayx():
    return [31, a(), 31,30,31,30,31,31,30,31,30,31]

def meses(a):
    def globalx():
        if (bisiesto(a)):
            return febrero29()
        else:
            return febrero28()

    anno = [31, globalx(), 31,30,31,30,31,31,30,31,30,31]
    return (anno)

def take(numMes, a):
    return (meses(a) [:numMes])

def numeroDia(d,m,a):
    return (( (a-1) * 365
              +(a-1)//4
              -(a-1)//100
              +(a-1)//400
              +sum(take(m-1,a))
              +d
              )% 7)
def d():
    return int(input(" Dia: "))

def m():
    return int(input(" Mes: "))

def a():
    return int(input(" Año: "))

def diaSemenaX(x):
    if (x) == 0:
        print("Estas en el dia 'Domingo'")
    elif x == 1:
        print("Estas en el dia 'Lunes'")
    elif x == 2:
        print("Estas en el dia 'Martes'")
    elif x == 3:
        print("Estas en el dia 'Miercoles'")
    elif x == 4:
        print("Estas en el dia 'Jueves'")
    elif x == 5:
        print("Estas en el dia 'Viernes'")
    else:
        print("Estas en el dia 'Sabado'")

print("--Introduce la fecha--")
diaSemenaX(numeroDia( d(),m(),a()))

# lambda x: x * 2