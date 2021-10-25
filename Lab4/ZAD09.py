print("Podaj liczbe:")
liczba = int(input())
lspace = liczba
char = "x"
space = " "
for i in range(0 , liczba):
    lspace -= 1
    print(lspace*space,char*(i+1))