"""
Some functions of operator with better type hints
"""

from operator import add, contains, getitem, is_, is_not, lshift, or_, rshift, sub

__all__ = (
    "is_",
    "is_not",
    "add",
    "sub",
    "contains",
    "rshift",
    "lshift",
    "getitem",
    # "or_",
    "itemgetter",
    "methodcaller",
    "attrgetter",
    # new functions
    "radd",
    "rsub",
    "argpasser",
    "pass_arg",
)


def pass_arg(arg, func, *args, **kwargs):
    return func(arg, *args, **kwargs)


def argpasser(arg, *args, **kwargs):
    def caller(func):
        nonlocal arg, args, kwargs
        return func(arg, *args, **kwargs)

    return caller


def radd(a, b):
    return b + a


def rsub(a, b):
    return b - a


def attrgetter(name: str):
    def caller(obj):
        nonlocal name
        return getattr(obj, name)

    return caller


def methodcaller(name: str, *args, **kwargs):
    def caller(obj):
        nonlocal args, kwargs, name
        return getattr(obj, name)(*args, **kwargs)

    return caller


def itemgetter(a):
    def __b(b):
        nonlocal a
        return b[a]

    return __b
