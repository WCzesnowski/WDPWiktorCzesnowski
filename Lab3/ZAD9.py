fa = 1
fb = 1
print(fa)
print(fb)
for i in range(28):
    temp = fb
    fb = fa + fb
    fa = temp
    print(fb)