def pascal_triangle():
    line = 0
    prevLine = [0, 1, 0]
    newLine = [0, 0]
    if line == 0:
        yield 1
    line += 1
    while True:
        for i in range(line + 1):
            newLine.insert(i+1, prevLine[i]+prevLine[i+1])
            yield newLine[i+1]
        prevLine = newLine.copy()
        newLine = [0, 0]
        line += 1
