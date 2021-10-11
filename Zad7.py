a = 5
b = 4

if a > 0 and b > 0:
    P = a*b
    if a == b:
        print("Prostokąt jest kwadratem!")
        print("Pole kwadratu wynosi:", P)
    else:
        print("Prostokąt nie jest kwadratem!")
        print("Pole prostokąta wynosi:", P)
else:
    print("Błędne dane")
    if a == b or a == -b or -a == b:
        print("Prostokąt jest kwadratem!")
        print("Boki kwadratu muszą być dodatnie")
    else:
        print("Prostokąt nie jest kwadratem")
        print("Boki prostokąta muszą być dodatnie")
