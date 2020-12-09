'''
Напишите декоратор @proﬁler, который при вызове функции будет сохранять в её атрибуты время ее исполнения (в секундах, можно дробное) и количество рекусивных вызовов произошедших при исполнении. Атрибуты назовите last_time_taken и calls.
Пользоваться глобальными переменными запрещено.
Декоратор должен вести себя порядочно, то есть не должен затирать документацию функции.
Сдавать нужно только код самого декоратора, тестирующий код импортирует его и прогонит набор тестов. Тестирующий код импортирует из вашего модуля декоратор и прогонит на наборе тестов.
Версия питона 3.4
Проверить работу ваших декораторов стоит на функции Аккермана и на функции, принимающей в себя произвольное число списков и склеивающей их в один. Обе этих функции реализуйте сами. Описание функции Аккермана см по ссылке. функция Аккермана
Аккермана удобно проверять с аргументами (3,4)).

Пример использования декоратора


import time


@profiler
def sleepy_recursion(num_calls):
    "I am a strange sleepy recursive function"
    time.sleep(1)
    if num_calls > 1:
        sleepy_recursion(num_calls - 1)


sleepy_recursion(3)

print(sleepy_recursion.__doc__)
print(sleepy_recursion.last_time_taken)
print(sleepy_recursion.calls)

I am a strange sleepy recursive function
3.003287
3
'''

from functools import wraps
import time


def profiler(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'recursion'):
            wrapper.recursion = True
            isReccured = False
        elif wrapper.recursion:
            isReccured = True
        else:
            isReccured = False
            wrapper.recursion = True

        if not hasattr(wrapper, 'calls') or not isReccured:
            wrapper.calls = 0

        wrapper.calls += 1
        startTime = time.time()
        res = func(*args, **kwargs)
        wrapper.last_time_taken = time.time() - startTime
        if not isReccured:
            wrapper.recursion = False
        return res

    return wrapper
