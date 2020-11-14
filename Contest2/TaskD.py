"""
Вам необходимо написать программу для вывода i-го простого числа.

Формат ввода
Одно число i - порядковый номер простого числа.

Формат вывода
i-е простое число.
"""

def primeNumber():
    primeNumbers = [2]
    yield primeNumbers[0]
    
    curNum = 3
    while(True):
        for i in primeNumbers:
            if curNum % i == 0:
                break
            elif i == primeNumbers[-1]:
                primeNumbers.append(curNum)
                yield curNum

        curNum += 1

num = int(input())
val = primeNumber()
for i in range(num - 1):
    next(val)
print(next(val))
