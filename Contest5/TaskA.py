'''
Напишите класс, который является расширением стандартного класса list. Сделайте так, чтобы, помимо обычных атрибутов в нем присутствовали такие:

reversed (с коротким псевдонимом R), который содержит тот же список, но с элементами в обратном порядке.
first (с коротким псевдонимом F), который содержит первый элемент списка. Должна присутствовать возможность изменять этот атрибут (и вместе с ним должен меняться и сам список). Атрибут не обязан работать корректно, если список пустой.
last (с коротким псевдонимом L), который содержит последний элемент списка. Должна присутствовать возможность изменять этот атрибут (и вместе с ним должен меняться и сам список). Атрибут не обязан работать корректно, если список пустой.
size (с коротким псевдонимом S), который содержит размер списка. Должна присутствовать возможность изменять этот атрибут: при увеличении размера в конец должны добавляться значения None, а при уменьшении последние элементы должны удаляться.
Обратите внимание, что все перечисленные атрибуты не являются методами (см. пример). Однако их рекомендуется не хранить, а вычислять «на лету».

Формат ввода
Ваш код должен иметь такой вид:

import sys

...

ваши импорты и реализация

класс должен называться «ExtendedList»

...

exec(sys.stdin.read())

(Программа выполнит код, записанный во входном файле)

Пример
Ввод
# this is for similar behaviour in python 2 and python 3
from __future__ import print_function


l = ExtendedList([1, 2, 3])
print(l.reversed)
print(l.first)
l.F = 0
print(l)
l.append(4)
print(l.L)
l.size = 2
print(l)

Вывод
[3, 2, 1]
1
[0, 2, 3]
4
[0, 2]
'''

import sys


class ExtendedList(list):

    alliases = {
        'R': 'reversed',
        'F': 'first',
        'L': 'last',
        'S': 'size'
    }

    def __init__(self, *args):
        super().__init__(*args)

    def __getattr__(self, name):
        name = self.alliases.get(name, name)
        if name == 'reversed':
            return [x for x in reversed(self)]
        elif name == 'first':
            return list.__getitem__(self, 0)
        elif name == 'last':
            return list.__getitem__(self, -1)
        elif name == 'size':
            return len(self)
        else:
            return list.__getattr__(self, name)

    def __setattr__(self, name, value):
        name = self.alliases.get(name, name)
        if name == 'first':
            list.__setitem__(self, 0, value)
        elif name == 'last':
            list.__setitem__(self, -1, value)
        elif name == 'size':
            if len(self) < value:
                list.extend(self, [None for i in range(value - len(self))])
            elif len(self) > value:
                for i in range(len(self) - value):
                    list.pop(self, -1)
        else:
            list.__setattr__(self, name, value)


exec(sys.stdin.read())
