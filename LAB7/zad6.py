def rysujdomek(x, z, y):
    def pietro():
        for _ in range(y):
            print(10 * x)
            print(3 * x + 4 * " " + 3 * x)
            print(3 * x + 4 * " " + 3 * x)
            print(10 * x)


    def dach():
        print(4 * " " + 2 * z + 4 * " ")
        print(3 * " " + 4 * z + 3 * " ")
        print(2 * " " + 6 * z + 2 * " ")
        print(" " + 3 * z + 2 * " " + 3 * z + " ")
        print(10 * z)

    dach()
    pietro()

rysujdomek("^","#", 3)
