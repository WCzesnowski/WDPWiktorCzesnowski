
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
for x in range(6):
        lista.append(a[x][x+1])
for x in range(5):
        lista.append(a[x][x+2])
for x in range(4):
    lista.append(a[x][x+3])
for x in range(3):
    lista.append(a[x][x+4])
for x in range(2):
    lista.append(a[x][x+5])
for x in range(1):
    lista.append(a[x][x+6])


for y in range(7):
    print(a[y])
print()
print()
print(lista)
print(sum(lista))
