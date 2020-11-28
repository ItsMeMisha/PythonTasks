string = input()
answer = dict()
i = 0
while i < len(string):
    if not string[i] in answer:
        answer[string[i]] = 1
    result = 1
    while (i < len(string) - 1) and (string[i] == string[i + 1]):
        result += 1
        i += 1
    answer[string[i]] = max(answer[string[i]], result)
    i += 1

for char in sorted(answer):
    print(char, answer[char])
