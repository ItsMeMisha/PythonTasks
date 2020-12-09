'''
Напишите декоратор @takes, который будет проверять правильность типов входных аргументов функции.
Декоратор принимает на вход типы аргументов и декорирует функцию таким образом, что она генеририрует исключение TypeError, если хотя бы один из аргументов имеет неверный тип.
Если аргументов больше, чем типов, то ошибку генерировать не нужно (возможно, точный тип известен только для первых аргументов, его, как раз, надо проверить).
Если типов больше, чем аргументов, то это тоже ошибка только в случае, если переданные аргументы не подходят под соответствующие им по порядку типы. (декоратор может быть применен к функциям с переменным числом аргументов).

Декоратор должен вести себя порядочно, то есть не должен затирать основные аргументы функции (__name__, __doc__, __module__).

Для простоты можно считать, что у функции нет именованных аргументов.

Генерацию исключений воспринимайте пока как волшебный способ просигнализировать об ошибке. Делается это так: raise TypeError
'''

import sys


from functools import wraps


def takes(*types):
    def actualDecorator(func):
        @wraps(func)
        def wrapper(*args):
            arg = iter(args)
            for atype in types:
                try:
                    if not isinstance(next(arg), atype):
                        raise TypeError
                except StopIteration:
                    pass
            return func(*args)

        return wrapper
    return actualDecorator

exec(sys.stdin.read())
