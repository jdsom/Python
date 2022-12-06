def palindrome(word):
    word = word.lower()
    reverse = word[::-1].lower()
    return word == reverse

print(palindrome("Wow"))