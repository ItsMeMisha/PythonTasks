"""
Как известно, счастливым билетиком называется такой, у которого сумма первых и последних трёх цифр равны. Напишите программу, которая для данного номера билетика найдёт ближайший к нему счастливый.
Формат ввода
Число из шести цифр.
Формат вывода
Ближайшее к данному число из шести цифр такое, что сумма первых трех равна сумме последних.

"""

inBounds = lambda num: num >= 0 and num < 1000000

lastThreeSum = lambda num: num % 10 + num // 10 % 10 + num // 100 % 10
firstHalf = lambda num: num // 1000
secondHalf = lambda num: num % 1000
isLucky = lambda num: lastThreeSum(firstHalf(num)) == lastThreeSum(secondHalf(num))

numUp = int(input())
numDown = numUp - 1
while inBounds(numUp) or inBounds(numDown):
    if inBounds(numUp):
        if isLucky(numUp):
            print(numUp)
            break
        else: 
            numUp += 1

    if inBounds(numDown):
        if isLucky(numDown):
            print(numDown)
            break
        else: 
            numDown -= 1
