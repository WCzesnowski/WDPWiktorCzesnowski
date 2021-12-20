
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
for i in range(0,len(dict4)):
    for j in range(0, len(dict3)):
        if i in dict4 == j in dict3:
            dict3[j] = dict3[j] + dict4[i]
            print(dict3[j])
print(dict3)