from random import shuffle

list = [1,2,3,4,5,6,7,8,9,10]
shuffle(list)
newlist = []
for element in list:
    if element >= 5: newlist.append(element)

print(newlist)

print([element for element in [1,2,3,4,5,6,7,8,9,10] if element < 5])