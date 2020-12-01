"""
В офисном здании проводят пожарные учения.

Сотрудники отдела безопасности хотят узнать, есть ли в здании люди. Для этого они хотят посмотреть логи пропускной системы, которая записывает все факты прикладывания пропусков сотрудники. Но, к сожалению, из-за ошибки в работе системы они не знают, входил человек или выходил. К счастью, так как офис на ночь закрывается и всех сотрудников выгоняют, можно восстановить эту информацию.

Так же они хотят найти лучший и худший момент времени для проведения учений:

- Лучшим моментом считается тот, в котором в здании было максимальное число сотрудников

- Худшим моментом считается самый первый момент (кроме начала дня), когда в здании нет сотрудников

Формат ввода
В одной строке через пробел передаются числа, которые соотвествуют ID приложенного пропуска в хронологическом порядке

Формат вывода
Через пробел выведите следующее:

1. True, если сейчас в здании не осталось ни одного человека, False иначе.

2. Самый ранний (за исключением начала дня) момент времени, когда в здании не было сотрудников. Момент времени определяется количеством записи в логе прямо перед ним. Например, начало дня - это 0, после прикладывания первого пропуска - 1 и т.д. Если такого момента нет, вывести 0.

3. Лучший момент для учений (если таких несколько, взять самый ранний).
"""

numbers = list(map(int, input().split(' ')))
people = set()
worse = 0
best = 0
bestNum = 0
time = 0
for card in numbers:
    time += 1
    if not card in people:
        people.add(card)
        if len(people) > bestNum:
            bestNum = len(people)
            best = time
    else:
        people.remove(card)
        if len(people) == 0 and worse == 0:
            worse = time

print(False, end=' ') if bool(people) else print(True, end=' ') 
print(worse , best)
    
