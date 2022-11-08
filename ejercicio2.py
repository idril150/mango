from functools import reduce
def sumar(x,y):
    return x+y
print(reduce(sumar,range(1,101)))