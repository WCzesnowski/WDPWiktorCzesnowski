liczba = input()
liczba = int(liczba)
binary = []
while liczba !=0:
    if liczba % 2 == 0:
        binary.append(0)
        liczba = liczba - (liczba/2)
    if liczba % 2 != 0:
        binary.append(1)
        liczba = liczba - (liczba/2) - 1
