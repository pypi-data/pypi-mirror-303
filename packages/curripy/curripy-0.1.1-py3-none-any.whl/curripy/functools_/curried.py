from functools import reduce as reduce_
from ..utils import curry


__all__ = ("reduce",)

reduce = curry(reduce_)
