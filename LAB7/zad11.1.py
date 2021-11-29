import math
def odleglosc(P1,P2):
    return math.sqrt(((P2[0] - P1[0]) * (P2[0] - P1[0])) + ((P2[1] - P1[1]) * (P2[1] - P1[1])))
def naJednejLinii(A,B,C):
    if A[0] * (B[1]-C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]) == 0:
        return True
    else:
        return False
def obwodTrojkota(A,B,C):
    if naJednejLinii(A,B,C) == False:
        return odleglosc(A,B) + odleglosc(A,C) + odleglosc(B,C)
    else:
        raise Exception("Punkty sa wspolliniowe!")
print(obwodTrojkota([0,0],[1,1],[2,2]))
