catNames = []
while True:
    name = input(f"Enter the name of your cat {str(len(catNames)+1)}: ")
    catNames += [name]
    if name == '':
        break
print("The cat names are:")
for name in catNames:
    print(f' {name}', end='')
