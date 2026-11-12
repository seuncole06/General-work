word = input("Enter a word: ")

isPalindrome = ""

for i in range(len(word) - 1, -1, -1):
    isPalindrome += word[i]

if word == isPalindrome:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
