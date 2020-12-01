from heapq import merge


def merge_sorter(*args):
    curMin = merge(*args)
    while True:
        try:
            yield next(curMin)
        except StopIteration:
            return
