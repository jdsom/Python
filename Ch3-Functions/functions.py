import random

def hello(name):
    print(f"Hello {name}.")

hello('Jordan')

def getAns(num):
    if num == 1:
        return 'low'
    elif num == 2:
        return 'mid'
    else:
        return 'high'
    
r = random.randint(1,4)
fortune = getAns(r)
print(fortune)