
A = [
    [1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1],
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
ruchy = 0
posg = A[c][u]
print(posg)
pos= A[y][x] = 2
print(pos)
for i in range(7):
    print(A[i])
while ruchy!=20:
    button = input()
    if button == 'w':
        A[y][x]=0
        if A[y-1][x] == 1:
            print("Uderzasz glową w ściane!")
        else:
            y -= 1
            ruchy += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                break
            for i in range(7):
                print(A[i])
    elif button == 's':
        if A[y+1][x] == 1:
            print("Uderzasz głową w ściane!")
        else:
            A[y][x] = 0
            y += 1
            ruchy += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                break
            for i in range(7):
                print(A[i])
    elif button == 'a':
        if A[y][x-1] == 1:
            print("Uderzasz głową w ściane!")
        else:
            A[y][x] = 0
            x -= 1
            ruchy += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                break
            for i in range(7):
                print(A[i])
    elif button == 'd':
        if A[y][x+1] == 1:
            print("Uderzasz głową w ściane!")
        else:
            A[y][x] = 0
            x += 1
            ruchy += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                break
            for i in range(7):
                print(A[i])
print("-------------")
for i in range(7):
    print(A[i])
print("Brawo!")
