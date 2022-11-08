def divisores(x):
    return (list(filter(lambda n: x % n == 0, list(range(1, x+1)))))


def primo(x):
    return (divisores(x) == [1, x])


def numerosPrimos(x):
    return (list(filter(primo, list(range(1, x+1)))))


print(numerosPrimos(int(input("introduce el numero: "))))
