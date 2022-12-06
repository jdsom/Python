def commaCode(listt):
    for inde, l in enumerate(listt):
        if l != listt[-1]:
            print(f"{l}, ", end="")
        else:
            print(f"{l}")

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)


