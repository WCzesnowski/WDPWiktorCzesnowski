
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
pos= A[y][x]
print(pos)
for i in range(5):
    button = input()
    if button == 'w':
        del pos
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

