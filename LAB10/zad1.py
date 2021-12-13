def permute(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r+1):
            if a[l] == a[i]:
                permute(a, l + 1, r)
                print("to samo")
            else:
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r)
                a[l], a[i] = a[i], a[l]
a = ['A', 'B', 'C', 'B']
permute(a, 0, len(a)-1)