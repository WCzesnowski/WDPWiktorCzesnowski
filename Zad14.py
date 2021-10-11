import math
a = 1
b = 5
c = 6

D=b*b - 4*a*c
if a!=0:
    if D < 0:
        print("Brak rozwiązań")
    if D == 0:
        x = -b / 2 * a
        print("Rozwiązanie wynosi:", x)
    if D > 0:
        g = (-b + math.sqrt(D)) / (2 * a)
        h = (-b - math.sqrt(D)) / (2 * a)
        print("Rozwiązania to:", g, h)
elif b == 0:
    if c == 0:
        print("Wiele rozwiązań")
    else:
        print("Zero rozwiązań")
else:
    x = -c/b
    print("Rozwiązanie to:", x)


