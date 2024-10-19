from typing import Any, Callable, Iterable

from typing_extensions import TypeIs

from ..__bootstrap.builtins_ import items, values
from ..__generics import ReturnT, ReturnT1, ReturnT2
from ..dummies.type import _ClassInfo
from ..utils import curry, curry_right, tap

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

# exported functions
hasattr_ = curry_right(hasattr)
print_ = tap(print)
help_ = tap(help)
startswith = curry_right(str.startswith, arity=2)

def next_(
    default: ReturnT2,
) -> Callable[[Iterable[ReturnT1]], ReturnT1 | ReturnT2]: ...
@curry_right
def isinstance_(
    obj: object,
    class_or_tuple: _ClassInfo,
) -> TypeIs[_ClassInfo]: ...

issubclass_ = curry_right(issubclass)

@curry
def setattr_(name: str, value: Any) -> Callable[[object], None]: ...
@curry
def getattr_(
    name: str, default: ReturnT | None = None
) -> Callable[[object], ReturnT | Any | None]: ...
