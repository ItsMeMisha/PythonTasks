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
    
