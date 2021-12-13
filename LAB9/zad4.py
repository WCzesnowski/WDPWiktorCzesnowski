def funkcja(n):
    if n == 0:
        return 0
    else:
        return funkcja(n-1)+n
print(funkcja(5))

def funkcja2(n):
    lista = []
    for i in range(1,n+1,1):
        lista.append(i)
    return sum(lista)

print(funkcja2(5))