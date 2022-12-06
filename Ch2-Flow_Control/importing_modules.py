import random, sys, os, math
for i in range(5):
    print(random.randint(1, 10))

response = ' '
while response:
    response = input(" Type exit to exit.\n")
    if response == 'exit':
        #sys.exit()
        break
    print(f"You typed {response}.")