
def szukajwliscie(lista, a):
     list = lista
     ilosc = 0
     for i in range(len(list)):
         if list[i] == a:
             ilosc += 1
     print("wynik:", ilosc)


szukajwliscie([2, 4, 5, 5, 6, 5, 4, 2, 5, 5], 5)


