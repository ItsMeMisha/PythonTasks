"""
Найдите большую из двух строк

Формат ввода
Программа принимает на вход две строки без пробелов

Формат вывода
Выведите большую из строк в лексикографическом порядке

Пример
Ввод	Вывод
aba
baa
baa

Примечания
В программе нельзя использовать условную конструкцию, тернарный условный оператор, и функцию max.

"""

string1 = input()
string2 = input()

firstBigger = string1 > string2
checker = {True: string1, False: string2}
print(checker[firstBigger])
