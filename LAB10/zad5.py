towar = [{'nazwa': 'banan', 'jednostka': 'kg', 'ilosc': 10, 'cena': 3},
         {'nazwa': 'jabłko', 'jednostka': 'kg', 'ilosc': 16, 'cena': 2.5},
         {'nazwa': 'mąka pszenna', 'jednostka': 'op.', 'ilosc': 30, 'cena': 2.5},
         {'nazwa': 'mydło', 'jednostka': 'szt.', 'ilosc': 6, 'cena': 1.5},
         {'nazwa': 'jogurt naturalny', 'jednostka': 'szt.', 'ilosc': 20, 'cena': 1.5},
         {'nazwa': 'papier toaletowy 8 rolek', 'jednostka': 'op.', 'ilosc': 10, 'cena': 9}]


def wyszukaj(towar, nazwa):
    x = False
    for i in range(0,len(towar)):
        if nazwa == towar[i]['nazwa']:
            print(towar[i])
            x = True
    if x == False:
        print('nie ma takiego towaru')

print('funkcja wyszukaj:')
wyszukaj(towar,'papier toaletowy 8 rolek')
print('-')
wyszukaj(towar,'masło')
print('')


def sumuj(towar, nazwa):
    x = False
    for i in range(0,len(towar)):
        if nazwa == towar[i]['nazwa']:
            y = float(towar[i]['ilosc'])
            z = float(towar[i]['cena'])
            print('cena sumarczyna wynosi:', y*z)
            x = True
    if x == False:
        print('nie ma takiego produktu')

print('funkcja sumuj:')
sumuj(towar,'jabłko')
print('-')
sumuj(towar,'masło')
print('')


def sumujWszystko(towar):
    lista = []
    for i in range(0,len(towar)):
        x = float(towar[i]['cena'])
        y = float(towar[i]['ilosc'])
        z = x*y
        lista.append(z)
    print(sum(lista))

print('funkcja sumujWszystko:')
sumujWszystko(towar)
print('')


def dodajTowar(towar, nazwa, jednostka, ilosc, cena):
    x = {'nazwa': nazwa,'jednostka': jednostka,'ilosc': ilosc,'cena': cena}
    towar.append(x)

print('funkcja dodajTowar')
dodajTowar(towar, 'brokuły', 'kg', 12, 10)
print('dodany towar:', towar[-1])
print('')


def aktualizujIlosc(towar, nazwa, ilosc):
    x = False
    for i in range(0,len(towar)):
        if nazwa == towar[i]['nazwa']:
            x = True
            ilosc = float(ilosc)
            towar[i]['ilosc'] = ilosc
            print(towar[i])
    if x == False:
        print('Podano błędną nazwe produktu')

print('funkcja aktualizujIlosc:')
aktualizujIlosc(towar, 'banan', 20)
print('')


def filtrJednostka(towar, jednostka):
    x = False
    print('')
    print('Podana jednostka:', jednostka)
    print('')
    for i in range(0,len(towar)):
        if jednostka == towar[i]['jednostka']:
            x = True
            print(towar[i])`
    if x == False:
        print('Żaden z produktów nie ma takiej jednostki')

print('funkcja filtrJednostka:')
filtrJednostka(towar, 'kg')

