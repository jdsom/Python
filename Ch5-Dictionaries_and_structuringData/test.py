spam = {'bar': 42}
spam.setdefault('color', 'black')

for k, v in spam.items():
    print(f"{k}: {v}")