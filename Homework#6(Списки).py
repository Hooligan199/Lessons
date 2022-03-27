g = [1,2,3,4,5,6,4,8,9,52,2,201]

h = [5,7,52,10,11,2,3,100,82,7456,100000,159852]

x = [x for x in g if x not in h]
x.extend([x for x in h if x not in g])

print(x)

