s = 2
amount = 0
liczba = input()
liczba = int(liczba)
zakres = liczba + liczba
while liczba > s:
    for i in range(2, zakres):
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                zakres
                s = i
                zakres += 10
                if s < liczba:
                    amount += 1
                else:
                    break
print(amount)