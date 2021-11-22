import math
def odleglosc(P1, P2, P3):
    list1 = P1
    list2 = P2
    list3 = P3
    AB = math.sqrt(((list2[0] - list1[0]) * (list2[0] - list1[0])) + ((list2[1] - list1[1]) * (list2[1] - list1[1])))
    AC = math.sqrt(((list3[0] - list1[0]) * (list3[0] - list1[0])) + ((list3[1] - list1[1]) * (list3[1] - list1[1])))
    BC = math.sqrt(((list3[0] - list2[0]) * (list3[0] - list2[0])) + ((list3[1] - list2[1]) * (list3[1] - list2[1])))
    wynik = AB + AC + BC
    return wynik

print(odleglosc([0, 0],  [0, 4], [3, 0]))