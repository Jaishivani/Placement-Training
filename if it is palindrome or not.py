def palin(s):
    return s == s[::-1]
w=input("Enter a word: ")
if palin(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
