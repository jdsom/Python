def iterativeSum(num): # iterates through loop until conditions are met
    summ = 0
    while num > 0:
        summ += num
        num -= 1
    return summ


def recursiveSum(num):  # calls function until conditions are met
    if num == 0:
        return 0
    else:
        return num + recursiveSum(num - 1)


print(iterativeSum(5))
print(recursiveSum(5))