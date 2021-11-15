from random import randint


print("odgadnij jaką liczbą jest x")

x = randint(1 , 100)
print(x)
próby = []
while True:
    button = input()
    button = int(button)
    if button == x:
        próby.append(button)
        print("brawo odgadłeś jaką liczbą jest x")
        print("liczba podjętych prób:", len(próby))
        break
    if button > x:
            print("Liczba którą podałeś jest większa od x")
            próby.append(button)
    if button < x:
            print("Liczba którą podałeś jest mniejsza od x")
            próby.append(button)

