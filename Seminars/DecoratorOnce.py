'''
Decorateor that calls a function only once
'''

import functools

def once(f):
    was_executed = False
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        nonlocal was_executed
        if not was_executed:
            was_executed = True
            return f(*args, **kwargs)
        else:
            print('!!!')
    return wrapped

@once
def add_one(x):
    return x + 1

print(add_one(1))
print(add_one(2))
