from ..__bootstrap.builtins_ import items, values
from ..utils import curry, curry_right, partial, tap

__all__ = (
    "getattr_",
    "hasattr_",
    "help_",
    "isinstance_",
    "issubclass_",
    "next_",
    "print_",
    "setattr_",
    "values",
    "startswith",
    "items",
)

hasattr_ = curry_right(hasattr)
print_ = tap(print)
help_ = tap(help)
isinstance_ = curry_right(isinstance, arity=2)
issubclass_ = curry_right(issubclass, arity=2)


def next_(default):
    return partial(next, default)


@curry
def setattr_(name, value):
    return partial(setattr, name, value)


@curry
def getattr_(name, default=None):
    def __get_object(o):
        nonlocal name
        nonlocal default
        return getattr(o, name, default)

    return __get_object


# methods
startswith = curry_right(str.startswith, arity=2)
