import math

lista = []
for a in range(1,50):
    for b in range(1,50):
        c = math.sqrt(a*a+b*b)
        if c < 50 and not any(c in temp for temp in lista):
            temp = [a,b,c]
            lista.append(temp)


for i in lista:
     print(i)
print("liczba trójek pitagorejskich:", lista.__len__())