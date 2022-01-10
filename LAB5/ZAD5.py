from random import randint
from random import seed

#wymiary tablicy
n = 7
m = 7
#sposób 1
lista = []
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    for j in range(m):
        a[i][j]= randint(0,20)
for x in range(7):
    x += 0
    lista.append(a[x][x])

print(a)
print(lista)
print(sum(lista))

