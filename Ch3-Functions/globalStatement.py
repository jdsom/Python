def spam():
    global eggs
    eggs = 'spam'


eggs = 'global' #refers to global variable
print(eggs)
spam()          #calls function which refers to local eggs as global variable
print(eggs)     #prints value spam