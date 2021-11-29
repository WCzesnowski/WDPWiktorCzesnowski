import math
def odleglosc(P1,P2):
    return math.sqrt(((P2[0] - P1[0]) * (P2[0] - P1[0])) + ((P2[1] - P1[1]) * (P2[1] - P1[1])))
def obwodTrojkota(A,B,C):
    return odleglosc(A,B) + odleglosc(A,C) + odleglosc(B,C)
print(obwodTrojkota([0,0],[0,4],[3,0]))


