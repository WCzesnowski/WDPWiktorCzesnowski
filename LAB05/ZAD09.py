
A = [
    [1,1,1,1,1,1,1],
    [1,2,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
]
x = 1
y = 1
c = 5
u= 5
posg = A[c][u]
print(posg)
pos= A[y][x]
print(pos)
while pos != posg:
    button = input()
    if button == 'w':
        y -= 1
    elif button == 's':
        y += 1
    elif button == 'a':
        x -= 1
    elif button == 'd':
        x += 1
for i in range(7):
    print(A[i])


print(y)
print(x)
newpos= A[y][x]
print(newpos)
for i in range(7):
    print(A[i])

