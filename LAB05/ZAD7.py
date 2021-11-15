from random import randint
n = 2
m = 3
y = []
x = []
z = []
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    for j in range(m):
        a[i][j]= randint(0,9)
for k in range(n):
    y.append(a[k][0])
    x.append(a[k][1])
    z.append(a[k][2])
print(a)
print(n)
print(m)

temp = n
n = m
m = temp
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    for j in range(m):
        a[i]= y,x,z

print(a)
print(a[1])






