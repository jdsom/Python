import random

num = random.randint(1, 10)
print("I'm thinking of a number between 1 and 20")
for x in range (1,10):
    guess = int(input("take a guess.\n"))
    if guess < num:
            print("too low")           
    elif guess > num:
            print("too high")         
    else:
         break

if guess == num:
    print(f"Correct! the number is {num}, that took you {str(x)} guesses! ")
else:
    print(f"The number I was thinking of was {num}")