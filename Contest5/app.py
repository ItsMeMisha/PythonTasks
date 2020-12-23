from functools import wraps

class VeryImportantClass:
    def __init__(self, i):
        self.i = i
        self.l = [1, 2, 3]

    def doSomeShit(a, b):
        print(a, b)

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('its shitty decorator')
        return func(*args, **kwargs)

    return wrapper
