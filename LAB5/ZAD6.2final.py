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
while n >=0:
    n -= 1
    for x in range(n):
        lista.append(a[x][x+(m-n)])

for z in range(m):
    print(a[z])
print()
print()
print(lista)
print(sum(lista))
