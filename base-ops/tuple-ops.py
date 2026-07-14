ntuple = tuple()
print(ntuple)

ntuple = (3,4,5,6,7,8)
print(ntuple)

for itm in ntuple:
    print(itm,end=" ")

# Tuple Concatenation
tup1 = (0, 1, 2, 3)
tup2 = ('Edo', 'For', 'Ishan')
tup3 = tup1 + tup2
print(tup3)

# Tuple Slicing
tup = tuple('EDOISHANLAGOS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])
