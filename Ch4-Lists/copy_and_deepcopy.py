import copy

# bacon = 'Hello'
# print(id(bacon))
# bacon += ' world!' # A new string is made from 'Hello' and ' world!'.
# print(f"{id(bacon)}\n") # bacon now refers to a completely different string.








# spam = 23 # int and strings are immutable
# print(id(spam)) 
# mapp = copy.copy(spam) # mapp and spam have the same reference
# print(id(mapp))

# spam += 1               # spam reference changes since int is immutable
# print(id(spam)) 
# print(id(mapp))         # mapp reference stays as original spam reference
# print(spam)             # prints 24
# print(mapp)             #prints 23
# print("\n")

spam = ['hi'] # int and strings are immutable
print(id(spam)) 
mapp = copy.copy(spam) # mapp and spam have the same reference
print(id(mapp))

spam.append('3')               # spam reference changes since int is immutable
print(id(spam)) 
print(id(mapp))         # mapp reference stays as original spam reference
print(spam)             # prints 24
print(mapp)             #prints 23
