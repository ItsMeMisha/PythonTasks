"""
Cейчас многие компании на программистских собеседованиях проводят предварительное тестирование. Классическая задача для такого тестирования — задача FizzBuzz.

Вам дано натуральное число N. Требуется вывести последовательность чисел от 1 до N. Но если число кратно 3, то выводится "Fizz"; если кратно 5, то "Buzz"; а если кратно 15, то "Fizz Buzz".

Поверьте, даже с такой простой задачей многие претенденты не справляются.

"""

num = int(input())
ending = ", "
for i in range(1, num + 1):
    if i == num:
        ending = '\n'

    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz", end = ending)
    elif i % 3 == 0:
        print("Fizz", end = ending)
    elif i % 5 == 0:
        print("Buzz", end = ending)
    else: 
        print(i, end = ending)
