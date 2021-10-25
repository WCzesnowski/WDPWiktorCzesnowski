print("Podaj imiona oddzielone przecinkami")
imiona = input()
im = imiona.split(' ')
lista = []
a ='a,'
for i in im:
    if i.endswith(a):
        lista.append(i)
print(lista)


