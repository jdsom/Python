allGuests = {'Jack': {'apples': 3, 'pears': 2}, 
            'Dave': {'apples': 3, 'ham sandwiches': 3},
            'Jones': {'pies': 2, 'pears': 5}}


def totalBrought(guests, item): # function with two parameters
    diffObjects = 0             # vairable to store number of items
    for k, v in allGuests.items(): # iterates through all key-values
        diffObjects += v.get(item, 0) # increments to variable
        # if item doesn't exist the set value 0 stays the same
    return diffObjects # returns total

print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
     