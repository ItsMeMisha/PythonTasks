string = input()
filtr = input()
result = ""
for char in string:
    if char in set(filtr) and char != ' ':
        continue
    result += char
print(result)
