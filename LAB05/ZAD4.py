from random import randint
from random import seed

#wymiary tablicy
n = 7
m = 10
#sposób 1
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    for j in range(m):
        a[i][j]= randint(0,20)
print(a)

