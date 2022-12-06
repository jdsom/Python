def collatz(number):
    if number % 2 == 0:
        return number
    else:
        return (3 * number )+ 1

try:
    n = ''
    while n != 1:
        n = int(input("Enter a number: "))
        print(collatz(n))
        
except ValueError:
    print("You must enter an integer.")