def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spamm(divideBy):
    return 42 / divideBy

try:
    spamm(1)
    spamm(2)
    spamm(0)
    spamm(12)
except ZeroDivisionError:
    print("You can't divide this value as it's invalid.")