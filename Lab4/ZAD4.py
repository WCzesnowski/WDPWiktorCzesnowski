print("Podaj boki prostokąta")
bok1 = input()
bok2 = input()
b1 = int(bok1)
b2 = int(bok2)
if b1 > 0 and b2 > 0:
    P = b1*b2
    Obw = (2*b1) + (2*b1)
    print("Pole prostokata:", P,", a obwod", Obw)
else:
    print(b1,"i",b2,"nie sa prawidlowymi bokami")