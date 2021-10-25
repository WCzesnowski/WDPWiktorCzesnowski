
lista = []
for x in range(3,100):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime:
        lista.append(x)
        if x-2 in lista:
            print(x-2 , x)



