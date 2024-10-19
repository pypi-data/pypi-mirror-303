from typing import Callable, TypeVar

from ..__bootstrap.operator_ import argpasser
from ..__generics import ParamT
from .curry_ import curry

ReturnThen = TypeVar("ReturnThen")
ReturnElse = TypeVar("ReturnElse")

__all__ = (
    "if_then_else",
    "if_then",
    "if_then_else_",
    "if_then_",
    "if_",
    "then",
    "else_",
)

def if_then_else_(
    c: Callable[[ParamT], bool],
    f: Callable[[ParamT], ReturnThen],
    e: Callable[[ParamT], ReturnElse],
    x: ParamT,
) -> ReturnThen | ReturnElse: ...
def if_then_(
    c: Callable[[ParamT], bool],
    f: Callable[[ParamT], ReturnThen],
) -> Callable[[ParamT], ReturnThen | ParamT]: ...

if_then_else = curry(if_then_else_, arity=4)
if_then = curry(if_then_, arity=2)
if_ = if_then_else

# FIXME type of then and else_ are incompatible with pipe
then = argpasser
else_ = argpasser
