def szukajwliscie(lista, a):
    list = lista
    wynik = 0
    for i in range(len(list)):
        if list[i] == a:
            wynik += 1
    return wynik

num = szukajwliscie([2, 4, 5, 5, 6, 5, 4, 2, 5, 5], 5)

print(num)


