import math
def odleglosc(P1,P2):
    return math.sqrt(((P2[0] - P1[0]) * (P2[0] - P1[0])) + ((P2[1] - P1[1]) * (P2[1] - P1[1])))
def obwodTrojkota(A,B,C):
    check = A[0] * (B[1]-C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])
    if (check == 0):
        raise Exception("Punkty sa wspolliniowe!")
    else:
        return odleglosc(A,B) + odleglosc(A,C) + odleglosc(B,C)
print(obwodTrojkota([0,0],[1,1],[2,2]))

