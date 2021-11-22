def obwod(P1, P2, P3):
    def odleglosc():
        list1 = P1
        list2 = P2
        wynik = math.sqrt(
            ((list2[0] - list1[0]) * (list2[0] - list1[0])) + ((list2[1] - list1[1]) * (list2[1] - list1[1])))
        return wynik
