from random import randint
from random import seed

#wymiary tablicy
n = 2
m = 3
#sposób 1
lista = []
a = [0] * n
x = [0] * m

for i in range(n):
    a[i] = [0] * m
    for j in range(m):
        a[i][j]= randint(0,20)
for i in range(m):
    x[i] = [0] * n
a[i][j] = x[i][j]
print(a)
print(x)