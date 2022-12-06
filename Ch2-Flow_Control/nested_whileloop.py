while True:
    name = input("What's your name: ")
    if name == 'exit':
        break
    else:
        password = input("Enter the password (it's a fish: " )
        while password != 'swordfish':
            print("Incorrect!")
            password = input("Enter the password (it's a fish: " )
        print(f"Password correct, Welcome {name}")
        break
