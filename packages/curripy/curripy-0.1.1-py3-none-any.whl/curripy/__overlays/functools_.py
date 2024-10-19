from functools import lru_cache

__all__ = (
    "lru_cache",
    "reduce_generator",
)

__initial_missing = object()


def reduce_generator(func, sequence, initial=__initial_missing):
    it = iter(sequence)
    try:
        value = next(it) if initial is __initial_missing else initial
    except StopIteration:
        raise TypeError("reduce() of empty iterable with no initial value") from None
    else:
        for element in it:
            value = func(value, element)
            yield value
