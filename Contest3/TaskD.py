string = input()
words = string.split(' ')
result = 0
for word in set(words):
    numberOfWord = 0
    for elem in words:
        if elem == word:
            numberOfWord += 1

    result = max(result, numberOfWord/len(words))
print(result)
