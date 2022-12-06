lol = 'Hi aNA ih'

def isPali(w):
    w = w.lower().replace(' ', '')
    rev = w[::-1]
    return w == rev

print(isPali(lol))