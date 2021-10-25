print("Podaj bok1")
bok1 = input()
b1 = int(bok1)
print("Podaj bok2")
bok2 = input()
b2 = int(bok2)
if b1 > 0 and b2 > 0:
    char = "x"
    for i in range(b1):
        print(char*b2)