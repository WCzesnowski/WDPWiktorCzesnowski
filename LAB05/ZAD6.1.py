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
y = 7
while y >=0:
    y -= 1
    for x in range(y):
        lista.append(a[x][x+(7-y)])

for z in range(7):
    print(a[z])
print()
print()
print(lista)
print(sum(lista))

