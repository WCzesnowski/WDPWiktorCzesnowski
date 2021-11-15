liczba = int(input("Podaj liczbę dodatnią: "))


i = 1
suma = []
while sum(suma)+i <= liczba:
    suma.append(i)
    i += 1


print(suma)
wynik = "W liczbie {} mieści się {} liczb pierwszych zaczynając od 1"
wynik = wynik.format(liczba, len(suma))
print(wynik)