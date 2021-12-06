lista = []
i = 0
while i < 10:
    button=input()
    x = str(button)
    lista.append(x)
    i += 1

for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)