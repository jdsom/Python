spam = {"name": "jordan", "age": 24, "Gender": "Male", "Programming Language": "Python"}

for k in spam.keys():
    print(f"{k}, ", end='')
print('\n')

for v in spam.values():
    print(f"{v}, ", end='')
print('\n')

for k, v in spam.items():
    print(f"{k}: {v}")

# using the setdefault() Method

spam.setdefault('colour', 'black')
print(spam)
spam.setdefault('colour', 'white') # since the key already has a value
# the value won't change
print(spam)

