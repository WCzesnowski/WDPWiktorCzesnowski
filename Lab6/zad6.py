
x = input()
x = int(x)
y = []
while x >= 1:

    temp = x % 10
    y.append(temp)
    x = x - temp
    x = x/10
print(sum(y))

