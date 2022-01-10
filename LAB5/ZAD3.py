from random import seed
from random import randint

# ziarno losowości, można wpisać dowolny numer
seed(111)
# losowa liczba całkowita z przedzialu od 0 do 10
x = randint(0, 10)
print(x)
