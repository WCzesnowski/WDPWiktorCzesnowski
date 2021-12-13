
dict1 = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2}
#1
print(dict(sorted(dict1.items(), key=lambda item: item[1])))
#2
dict2 = {8: 10, 9: 40, 10: 34, 11: 100}
dict3 = {**dict1, **dict2}
print(dict3)
#3
print(sum(dict3.values()))
#4
dict4 = {1: 10, 3: 50, 6: 4, 10: 2}
dict3.update(dict4)
print(dict3)