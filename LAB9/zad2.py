lista = []
i = 0
while i < 10:
    button=input()
    lista.append(button)
    i += 1
lista.reverse()
print(lista)
print(sorted(lista)[-1])