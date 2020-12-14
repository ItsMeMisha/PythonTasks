'''
Чудесная штука – исключения. В комплекте же с контекстными менеджерами их возможности возрастают многократно.
Напишите несколько контекстных менеджеров для обработки исключений.
Глушитель исключений

with supresser(type_one, ...): 
    do_smth()
перехватывает исключения заданых (и только заданных) типов и возвращает управление потоку. Исключение не пробрасывается дальше
Переименователь исключений

with retyper(type_from, type_to): 
    do_smth()
меняет тип исключения, оставляя неизменными содержимое ошибки (атрибут args) и трейсбек. Исключение пробрасывается дальше
Дампер исключений

with dumper(stream): 
    do_smth()
записывает в объект stream тело и трейсбек исключения в необычном порядке: сначала ошибка, потом трейсбек исключение пробрасывается дальше.
предполагается что у объекта stream обязательно должен быть метод write (для отладки можно использовать io.StringIO())
Пример использования retyper

> cat use_retyper.py 
import managers 
 
def foo(): 
    i = 1 / 0 
 
 
with managers.retyper(ZeroDivisionError, KeyError): 
    foo() 
> python3 use_retyper.py
выведет
Traceback (most recent call last): 
  File "/Users/veronikaiv/Desktop/managers.py", line 16, in retyper 
    yield 
  File "use_retyper.py", line 8, in <module> 
    foo() 
  File "use_retyper.py", line 4, in foo 
    i = 1 / 0 
ZeroDivisionError: division by zero 
 
During handling of the above exception, another exception occurred: 
 
Traceback (most recent call last): 
  File "use_retyper.py", line 8, in <module> 
    foo() 
 [censored] 
  File "use_retyper.py", line 8, in <module> 
    foo() 
  File "use_retyper.py", line 4, in foo 
    i = 1 / 0 
KeyError: ’division by zero’
Пример использования supresser

cat use_supresser.py 
import managers 
import sys 
 
def foo(): 
    a = {} 
    a[1] 
 
 
with managers.supresser(ValueError, KeyError): 
    foo() 
 
with managers.supresser(KeyError): 
    1 / 0 
 
> python3 use_supresser.py
выведет
Traceback (most recent call last): 
  File "use_supresser.py", line 13, in <module> 
    1 / 0 
ZeroDivisionError: division by zero
Пример использования dumper

> cat use_dumper.py 
import managers 
import sys 
 
def foo(): 
    i = 1 / 0 
 
 
with managers.dumper(sys.stderr): 
    foo() 
> python3 dumper.py
выведет
ZeroDivisionError: division by zero 
Traceback (most recent call last): 
  File "use_dumper.py", line 9, in <module> 
    foo() 
  File "use_dumper.py", line 5, in foo 
    i = 1 / 0 
ZeroDivisionError: division by zero
Пример
Ввод	Вывод
Примечания
Вам может пригодиться упрощённый способ создания контекстных менеджеров https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
Обратите внимание, что менеджер supress надо реализовывать самостоятельно.

'''
