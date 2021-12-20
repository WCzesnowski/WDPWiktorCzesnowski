x = open("liczby.txt", "x")
for i in range(1,100):
    x.write(str(i))
    x.write("\n")
x = open('liczby.txt', 'r')
print(x.read())