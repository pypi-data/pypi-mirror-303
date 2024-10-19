from typing_extensions import TypeIs

from ..__bootstrap.builtins_ import filter_, map_
from ..dummies.type import _ClassInfo
from ..utils import curry, curry_right

__all__ = (
    "divmod_",
    "rdivmod",
    "map_",
    "filter_",
)

issubclass_ = curry(issubclass)
divmod_ = curry(divmod)
rdivmod = curry_right(divmod)

@curry
def isinstance_(
    obj: object,
    class_or_tuple: _ClassInfo,
) -> TypeIs[_ClassInfo]: ...

getattr_ = curry(getattr)
setattr_ = curry(setattr)
