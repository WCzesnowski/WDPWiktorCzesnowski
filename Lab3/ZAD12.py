k = [6, 5, 3, 8, 17, 13, 19]
min= k[0]
max= k[0]
for i in k:
    if i < min:
        min = i
    if i > max:
        max = i
print(min)
print(max)
