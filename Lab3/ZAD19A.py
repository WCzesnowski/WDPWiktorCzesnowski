lista = []
blizniaki = []
for x in range(2,100):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime:
       lista.append(x)

for i in lista:
    if i+2 in lista:
        temp = [i,i+2]
        blizniaki.append(temp)

for i in blizniaki:
    print(i)
print("Ilosc blizniakow:" ,blizniaki.__len__())