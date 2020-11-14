"""
Переведите число из десятеричной системы счисления в некоторую другую

Формат ввода
На вход подается одна строка, в которой записано число в десятеричной системе счисления и основание новой (не превышающее 9)

Формат вывода
Введите число в новой системе счисления
"""

num, base = map(int, input().split())
curNum = 0
curMultiplier  = 1
while num != 0:
    curNum = curNum + (num % base) * curMultiplier
    num //= base
    curMultiplier *= 10

print(curNum)
