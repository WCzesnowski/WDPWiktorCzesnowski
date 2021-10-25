iloscLiczb = 0

for x in range(2,100):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime:
       iloscLiczb += 1
       print (x)
print("Ilosc liczb pierwszych:" ,iloscLiczb)
