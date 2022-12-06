print('Hello'.rjust(10)) # Justify 'Hello' with total string 
                         # length of 10
print('Hello'.ljust(10) + ' wgrwgrwg')
print('Hello'.center(10))

#adds white space either on left, right or both sides of the string


print('Hello'.center(20, '-'))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print(f"{'PICNIC ITEMS'.center(leftWidth + rightWidth, '-')}")
    for k, v in itemsDict.items():
        print(f"{k.ljust(leftWidth, '.')}{str(v).rjust(rightWidth)}")


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)