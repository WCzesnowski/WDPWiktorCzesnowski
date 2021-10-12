a = 9
b = 7
c = 7


if c > b and c > a and c < (a+b):
    if (a * a) + (b * b) == (c * c):
        if a == b == c:
            print("Trójkąt prostokątny, równoboczny")
        else:
            print("Trójkąt prostokątny, różnoboczny")
    if (a * a) + (b * b) < (c * c):
        if a == b:
            print("Trójkąt rozwartokątny, równoramienny")
        else:
            print("Trójkąt rozwartokątny, różnoboczny")
    if (a * a) + (b * b) > (c * c):
        if a == b:
            print("Trójkąt ostrokątny, równoramienny")
        else:
            print("Trójkąt ostrokątny, różnoboczny")


if a > b and a > c and a < (c+b):
    if (c * c) + (b * b) == (a * a):
        if a == b == c:
            print("Trójkąt prostokątny, równoboczny")
        else:
            print("Trójkąt prostokątny, różnoboczny")
    if (c * c) + (b * b) < (a * a):
        if c == b:
            print("Trójkąt rozwartokątny, równoramienny")
        else:
            print("Trójkąt rozwartokątny, różnoboczny")
    if (c * c) + (b * b) > (a* a):
        if c == b:
            print("Trójkąt ostrokątny, równoramienny")
        else:
            print("Trójkąt ostrokątny, różnoboczny")

if b > a and b > c and b < (c+a):
    if (c * c) + (a * a) == (b * b):
        if a == b == c:
            print("Trójkąt prostokątny, równoboczny")
        else:
            print("Trójkąt prostokątny, różnoboczny")
    if (c * c) + (a * a) < (b * b):
        if c == a:
            print("Trójkąt rozwartokątny, równoramienny")
        else:
            print("Trójkąt rozwartokątny, różnoboczny")
    if (c * c) + (a * a) > (b* b):
        if c == a:
            print("Trójkąt ostrokątny, równoramienny")
        else:
            print("Trójkąt ostrokątny, różnoboczny")
else:
    print("To nie są boki trójkąta")




