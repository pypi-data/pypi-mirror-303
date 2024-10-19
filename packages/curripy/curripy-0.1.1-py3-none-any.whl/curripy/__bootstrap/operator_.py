from ..__overlays.operator_ import attrgetter, itemgetter, methodcaller
from ..__overlays.operator_ import pass_arg, argpasser

__all__ = (
    # normal functions
    "add",
    "radd",
    "is_",
    "is_not",
    "or_",
    "contains",
    # new functions
    "pass_arg",
    "argpasser",
    "attrgetter",
    "itemgetter",
    "methodcaller",
    "radd",
)


def add(a):
    def __b(b):
        nonlocal a
        return a + b

    return __b


def radd(a):
    def __b(b):
        nonlocal a
        return b + a

    return __b


def is_(a):
    def __b(b):
        nonlocal a
        return a is b

    return __b


def is_not(a):
    def __b(b):
        nonlocal a
        return a is not b

    return __b


def or_(a):
    def __b(b):
        nonlocal a
        return a | b

    return __b


def in_(a):
    def __b(b):
        nonlocal a
        return b in a

    return __b


# pointfree style functions
def contains(b):
    def __a(a):
        nonlocal b
        return b in a

    return __a
