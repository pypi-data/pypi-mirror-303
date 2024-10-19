from functools import reduce

from curripy.__bootstrap.identity_ import identity

from .operator_ import pass_arg

__all__ = (
    "dot",
    "cdot",
    "compose",
    "pipe",
)


def cdot(f):
    def __dot(g):
        def caller(x):
            nonlocal f
            nonlocal g
            return g(f(x))

        return caller

    return __dot


def dot(f, g):
    def caller(x):
        nonlocal f
        nonlocal g
        return g(f(x))

    return caller


def __define_order(order):
    def portal(*funcs):
        nonlocal order

        def reducer(instance=None):
            nonlocal funcs
            return reduce(pass_arg, order(funcs), instance)

        if len(funcs) < 1:
            return identity
        elif len(funcs) == 1:
            func, *_ = funcs
            return func

        return reducer

    return portal


pipe = __define_order(identity)
compose = __define_order(reversed)
