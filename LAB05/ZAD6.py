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

        #      (0.1)(0.2)(0.3)(0.4)(0.5)(0.6)
        #           (1.2)(1.3)(1.4)(1.5)(1.6)
        #                (2.3)(2.4)(2.5)(2.6)
        #                     (3.4)(3.5)(3.6)
        #                          (4.5)(4.6)
        #                               (5.6)

for x in range(6):
    for y in range(5):
        y += 0
        x += 0
        x + y =
        lista.append(a[y][x])


print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print()
print()
print(lista)
print(sum(lista))

