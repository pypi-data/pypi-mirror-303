from ..__bootstrap.operator_ import argpasser
from .partial_ import partial
from .curry_ import curry
from .identity_ import identity

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
    c,
    f,
    e,
    x,
):
    return f(x) if c(x) else e(x)


def if_then_(
    c,
    f,
):
    return partial(if_then_else_, c, f, identity)


if_then_else = curry(if_then_else_, arity=4)
if_then = curry(if_then_, arity=2)
if_ = if_then_else
then = argpasser
else_ = argpasser
