def factorize(n):
    for num in range(1, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if n % num == 0 and n>1:
                    print(num)
                    factorize(n // num)

print(factorize(1470))