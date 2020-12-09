'''
Бывает полезно оптимизировать вызовы "тяжёлых"функций с помощью кеширования. Кеширование – это сохранение результатов выполнения функций для предотвращения повторных вычислений. Перед вызовом функции проверяется есть ли уже вычисленный результат. Если есть – функция не вызывается, а возвращается сохранённое значение.
Реализуйте декоратор для Least Recently Used (LRU) Cache. Пользователь указывает размер кеша N, и в кеше сохраняются N последних вычислений. Другими словами, вытесняется из кеша сначало то, что использовалось давней всего.
Декоратор назовите @cache, он должен принимать один параметр – размер кеша. Поддержите как можно более широкий класс функций (функции многих аргументов, функции с именоваными параметрами, принимающие сложные типы итд). Декоратор должен вести себя порядочно, то есть не должен затирать документацию функции.
Пример работы
Вот такой код
@cache(2) 
def foo(value): 
        print(’calculate foo for {}’.format(value)) 
        return value 
 
foo(1) 
foo(2) 
foo(1) 
foo(2) 
foo(3) 
foo(1)
должен произвести такой вывод
calculate foo for 1 
calculate foo for 2 
calculate foo for 3 
calculate foo for 1
'''

from functools import wraps
from collections import OrderedDict


def make_key(*args, **kwargs):
    return (args, (tuple(kwargs.keys()), tuple(kwargs.values())))


def cache(size):
    def actualDecorator(func):
        cache = OrderedDict({})

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = make_key(*args, **kwargs)
            if key not in cache:
                if len(cache) == size:
                    cache.popitem(last=False)
                res = func(*args, **kwargs)
                cache.update({key: res})
                cache.move_to_end(key)
            return cache[key]

        return wrapper
    return actualDecorator
