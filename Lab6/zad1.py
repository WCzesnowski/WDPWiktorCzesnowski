liczba = int(input("Podaj liczbę dodatnią: "))

i = 1
suma = 0

while i <= liczba:
    suma = suma + i
    i += 1

wynik = "Suma wszystkich liczb naturalnych niewiększych niż {} wynosi {}"
wynik = wynik.format(liczba, suma)
print(wynik)