a = 3
b = 4
c = 3

if a < b:
    if a < c:
        print("a jest najmniejsze")
    if a == c:
        print("a i c są najmniejsze")
    else:
        print("c jest najmniesze")
if b < a:
    if b < c:
        print("b jest najmniejsze")
    if b == c:
        print("b i c są najmniejsze")
    else:
        print("c jest najmniejsze")
if a == b == c:
    print("Wszystkie liczby są równe")
