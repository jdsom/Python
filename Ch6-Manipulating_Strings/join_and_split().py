animals = ['cats','dogs','bats'] # calls a list and returns a string
print(', '.join(animals))

animals = ['cats','dogs','bats']
print(' '.join(animals))

animals = ['my','name','is', 'jordan']
print('ABC'.join(animals))
print("\n")

print('MyABCnameABCisABCJordan'.split('ABC')) # calls a string and returns a list



spam = '''Hello,
Today we are going to show you how to use split()
to split multiple lines
every line will be an element in a list using spam.split(\n)'''

print(spam.split('\n'))
