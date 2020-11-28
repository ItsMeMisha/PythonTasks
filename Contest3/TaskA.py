string = input()
print(not (False in [False if string[i] in set(string[:i]+string[i+1:]) else True for i in range(len(string))]))
