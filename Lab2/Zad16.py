import math
x = 1567
t = math.floor(x/1000)
s = math.floor((x - t*1000)/100)
d = math.floor((x - t*1000 - s*100)/10)
j = math.floor((x - t*1000 - s*100 - d*10))
if x>99 and x<9999:
    print(t)
    print(s)
    print(d)
    print(j)
else:
    print("Błędna Liczba")







