"""
В этой задаче требуется вывести массив размера N × M, в котором на месте (i,j) стоит произведение i × j.

Эту задачу можно (но необязательно) решить в одну строку.

Формат ввода
Два числа: N и M.

Формат вывода
Массив размера N × M, в котором числа разделены пробелами.

Обратите внимание, для подсчёта произведений используется 1-индексация.

"""

numOfStrings, numOfColoumns = map(int, input().split())
for i in range(1, numOfStrings + 1):
    for j in range(1, numOfColoumns + 1):
        print(i*j, end=' ')
    print()
