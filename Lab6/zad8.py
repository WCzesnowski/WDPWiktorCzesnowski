
A = [
    [1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
]
x,y = 1,1
c,u = 5,5
moves = 0
posg = A[c][u]
pos= A[y][x] = 2
for i in range(7):
    print(A[i])
while moves!=20:
    button = input()
    if button == 'w':
        A[y][x]=0
        if A[y-1][x] == 1:
            moves += 1
            print("Uderzasz glową w ściane!")
        else:
            y -= 1
            moves += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                print("Brawo!")
                break
            for i in range(7):
                print(A[i])
    elif button == 's':
        if A[y+1][x] == 1:
            moves += 1
            print("Uderzasz głową w ściane!")
        else:
            A[y][x] = 0
            y += 1
            moves += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                print("Brawo!")
                break
            for i in range(7):
                print(A[i])
    elif button == 'a':
        if A[y][x-1] == 1:
            moves += 1
            print("Uderzasz głową w ściane!")
        else:
            A[y][x] = 0
            x -= 1
            moves += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                print("Brawo!")
                break
            for i in range(7):
                print(A[i])
    elif button == 'd':
        if A[y][x+1] == 1:
            moves += 1
            print("Uderzasz głową w ściane!")
        else:
            A[y][x] = 0
            x += 1
            moves += 1
            pos = A[y][x] = 2
            if y==c and x==u:
                print("Brawo!")
                break
            for i in range(7):
                print(A[i])
print("-------------")
if y!=c and x!=u:
    print("Przykro mi. Nie udało ci się dojść do celu w 20 ruchów.")
for i in range(7):
    print(A[i])

