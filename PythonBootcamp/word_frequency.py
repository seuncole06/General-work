def word_frequency(sentence):
    sentence = sentence.lower()

    words = sentence.split("")
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input("Enter a sentence: ")
result = word_frequency(sentence)
print(result)
