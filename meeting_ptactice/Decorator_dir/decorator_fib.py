# encoding:utf-8
from functools import wraps

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        reslut = cache.get(args, miss)
        if reslut is miss:
            reslut = fn(*args)
            cache[args] = reslut
        return reslut

    return  wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)




print(fib(2))