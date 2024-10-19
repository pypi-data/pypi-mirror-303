from curripy.utils.curry_ import curry_right
from ..utils import curry
from ..__bootstrap.builtins_ import map_, filter_

__all__ = (
    "divmod_",
    "rdivmod",
    "map_",
    "filter_",
)

divmod_ = curry(divmod)
rdivmod = curry_right(divmod)
isinstance_ = curry(isinstance, arity=2)
issubclass_ = curry(issubclass, arity=2)


# not exported
@curry
def getattr_(o, name, default=None):
    return getattr(o, name, default)


@curry
def setattr_(o, name, value):
    return setattr(o, name, value)
