word1 = input("Enter a word: ").lower()
word2 = input("Enter another word: ").lower()
anagram = {}
for letter in word1:
    if letter in anagram:
        anagram[letter] += 1
    else:
        anagram[letter] = 1

for letter in word2:
    if letter in anagram:
        anagram[letter] -= 1
    else:
        anagram[letter] = 1

if all(count == 0 for count in anagram.values()):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")