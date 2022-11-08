def divisible(t,n):
    return (t % n == 0)

def bisisestro (a):
    return(divisible(a,4) and (not(divisible(a,100))or divisible(a,400)))

def meses (a):
    if(bisisestro(a)):
        feb = 29
    else:
        feb = 28
    anno = [31,feb,31,30,31,30,31,31,30,31,30,31]
    return(anno)

def take(numMes,a):
    return(meses(a)[:numMes])

def numeroDia(fecha):
    return((  (int(fecha[2])-1)*365
            +(int(fecha[2])-1)//4
            -(int(fecha[2])-1)//100
            +(int(fecha[2])-1)//400
            +sum(take(int(fecha[1])-1,int(fecha[2])))
            +int(fecha[0])
            )%7)

print("introduce la fecha: ")
d = int(input("dia: "))
m = int(input("mes: "))
a = int(input("año: "))
diaSemana = numeroDia(d,m,a)
if diaSemana == 0:
    print("Domingo")
elif diaSemana == 1:
    print("Lunes")
elif diaSemana == 2:
    print("Martes")
elif diaSemana == 3:
    print("Miercoles")
elif diaSemana == 4:
    print("Jueves")
elif diaSemana == 5:
    print("Viernes")
else:
    print("Sabado")



