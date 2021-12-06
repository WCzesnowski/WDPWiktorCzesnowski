A = [
    [1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
]
def rysujLabirynt(macierz, puste, sciana, ludzik, drzwi):
    A = macierz
    for x in range(7):
        for y in range(7):
            if A[x][y] == 1:
                A[x][y] = sciana
            elif A[x][y] == 0:
                A[x][y] = puste
            elif A[x][y] == 2:
                A[x][y] = ludzik
            elif A[x][y] == 3:
                A[x][y] = drzwi
    for i in range(7):
        print(A[i])

def aktualizujLabirynt(moves):
    x, y = 1, 1
    A[x][y] = 2
    while moves != 0:
        button = input()
        if button == 'w':
            A[x][y] = 0
            if A[y - 1][x] == 1:
                moves -= 1
                print("Uderzasz glową w ściane!")
            elif A[y - 1][x] == 3:
                print("Brawo")
                break
            else:
                y -= 1
                moves -= 1
                A[y][x] = 2
            rysujLabirynt(A," ", "#", "o", "x")
        elif button == 's':
            if A[y + 1][x] == 1:
                moves -= 1
                print("Uderzasz głową w ściane!")
            elif A[y + 1][x] == 3:
                print("Brawo")
                break
            else:
                A[y][x] = 0
                y += 1
                moves -= 1
                A[y][x] = 2
            rysujLabirynt(A," ", "#", "o", "x")
        elif button == 'a':
            if A[y][x - 1] == 1:
                moves -= 1
                print("Uderzasz głową w ściane!")
            elif A[y][x - 1] == 3:
                print("Brawo")
                break
            else:
                A[y][x] = 0
                x -= 1
                moves -= 1
                A[y][x] = 2
            rysujLabirynt(A," ", "#", "o", "x")
        elif button == 'd':
            if A[y][x + 1] == 1:
                moves -= 1
                print("Uderzasz głową w ściane!")
            elif A[y][x+1] == 3:
                print("Brawo")
                break
            else:
                A[y][x] = 0
                x += 1
                moves -= 1
                A[y][x] = 2
            rysujLabirynt(A, " ", "#", "o", "x")

def gra(macierz ,n):
    rysujLabirynt(macierz ," ", "#", "o", "x")
    while n>1:
        aktualizujLabirynt(n)


gra(A, 20)