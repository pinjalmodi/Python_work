l=[1,2,3,4,5,6,7,8,9]

del l[0]
del l[4]
del l[5]

print(l)


print("-----------------------------")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]


print(color)
