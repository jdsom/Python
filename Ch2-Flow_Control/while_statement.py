name = ''
while name != 'end':
    name = input("Enter your name:\n ")
    print(f"Hello {name}!")

spam = 0
while spam < 6:
    print(f"spam is currently {spam}")
    spam += 1

while True:
    print("Enter your name:")
    name = input()
    if name == "your name":
        break
    else:
        print(f"Hello {name}!")
        
print("Thank you!")