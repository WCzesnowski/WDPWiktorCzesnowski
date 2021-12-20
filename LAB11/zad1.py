import time
import random
start = time.time()
lista = []
for k in range(1000):
    x = random.randrange(1000)
    lista.append(x)
for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
end = time.time()
print(end-start)