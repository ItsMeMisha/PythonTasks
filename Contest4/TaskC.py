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
