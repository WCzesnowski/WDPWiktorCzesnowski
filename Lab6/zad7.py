import math
liczba = input()
liczba = int(liczba)

binary = []
while liczba !=0:
    if liczba % 2 == 0:
        binary.append(0)
        liczba = (liczba/2)
    else:
        binary.append(1)
        liczba = math.floor(liczba/2)
binary.reverse()
print(binary)