animals = ['dog','cat','bird']
animals.append('rat') #adds element to end of the list
for a in animals:
    print(a)
print()

animals.insert(0,'dragon') #argument is index position and value
for a in animals:
    print(a)
print()

animals.remove('cat')
for a in animals:
    print(a)
print()

animals.sort()
for a in animals:
    print(a)
print()