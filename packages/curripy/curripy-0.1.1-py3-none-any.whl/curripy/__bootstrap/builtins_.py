from .operator_ import methodcaller

__all__ = (
    "filter_",
    "map_",
    "values",
    "keys",
)


def filter_(func):
    def caller(iterable):
        return filter(func, iterable)

    return caller


def map_(func):
    def caller(*iterables):
        return map(func, *iterables)

    return caller


values = methodcaller("values")
items = methodcaller("items")
keys = methodcaller("keys")
