import math
def binary(n):
    if n > 0:
        print(n)
        lista = []
        if n%2!=0:
            lista.append(1)
        else:
            lista.append(0)
        print(lista)
        return binary(math.floor(n/2))
print(binary(156))