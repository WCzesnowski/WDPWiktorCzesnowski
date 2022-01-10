from random import randint
from random import seed


n = 3
m = 5

a = [0] * n
for i in range(n):
    a[i] = [0] * m
    for j in range(m):
        a[i][j]= randint(0,20)
print(a)

o = 5
p = 4

b = [0] * o
for i in range(o):
    b[i] = [0] * p
    for j in range(p):
        b[i][j]= randint(0,20)


result = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],]

for i in range(len(b)):
    for j in range (len(a[0])):
        for k in range (len(a)):
            result[i][j] += a[i][k] * b[k][j]

for r in result:
    print(r)