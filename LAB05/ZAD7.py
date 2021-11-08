
n = 2
m = 3

a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)
print(n)
print(m)
temp = n
n = m
m = temp
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(n)
print(m)
print(a)

