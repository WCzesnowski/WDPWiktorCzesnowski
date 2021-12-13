def Euk(a, b):
    if b != 0:
        return Euk(b,a%b)
    return a

print(Euk(28, 24))

def Euk2(a ,b):
    while a != b:
        if(a>b):
                a = a - b
        else:
            b = b - a
    return a

print(Euk(12, 18))
