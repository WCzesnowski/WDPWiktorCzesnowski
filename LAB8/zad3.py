def tiles(n, k):
    if n == 1:
        return k
    else:
        return tiles(n-1,k) + (2 * n - 1) * tiles(1,k)

print(tiles(3,6))