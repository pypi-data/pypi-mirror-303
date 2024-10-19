from typing import (
    Callable,
    Concatenate,
    Literal,
    overload,
)

from ..__generics import ArgKwargP, ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT

__all__ = (
    "curry",
    "curry_right",
)

# FIXME the generic type only picks the first overloaded type
@overload
def curry(
    func: Callable[[ParamT1], ReturnT],
    arity: None = ...,
) -> Callable[[ParamT1], ReturnT]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2], ReturnT],
    arity: None = ...,
) -> Callable[[ParamT1], Callable[[ParamT2], ReturnT]]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2, ParamT3], ReturnT],
    arity: None = ...,
) -> Callable[[ParamT1], Callable[[ParamT2], Callable[[ParamT3], ReturnT]]]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4], ReturnT],
    arity: None = ...,
) -> Callable[
    [ParamT1],
    Callable[[ParamT2], Callable[[ParamT3], Callable[[ParamT4], ReturnT]]],
]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5], ReturnT],
    arity: None = ...,
) -> Callable[
    [ParamT1],
    Callable[
        [ParamT2],
        Callable[[ParamT3], Callable[[ParamT4], Callable[[ParamT5], ReturnT]]],
    ],
]: ...
@overload
def curry(
    func: Callable[ArgKwargP, ReturnT],
    arity: Literal[1],
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamT1, ArgKwargP], ReturnT],
    arity: Literal[2],
) -> Callable[[ParamT1], Callable[ArgKwargP, ReturnT]]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamT1, ParamT2, ArgKwargP], ReturnT],
    arity: Literal[3],
) -> Callable[[ParamT1], Callable[[ParamT2], Callable[ArgKwargP, ReturnT]]]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamT1, ParamT2, ParamT3, ArgKwargP], ReturnT],
    arity: Literal[4],
) -> Callable[
    [ParamT1],
    Callable[[ParamT2], Callable[[ParamT3], Callable[ArgKwargP, ReturnT]]],
]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP],
        ReturnT,
    ],
    arity: Literal[5],
) -> Callable[
    [ParamT1],
    Callable[
        [ParamT2],
        Callable[[ParamT3], Callable[[ParamT4], Callable[ArgKwargP, ReturnT]]],
    ],
]: ...
@overload
def curry(
    func: Callable[ArgKwargP, ReturnT],
    arity: int | None = ...,
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> Callable[..., ReturnT]: ...
@overload
def curry_right(
    func: Callable[[ParamT1], ReturnT],
    arity: None = ...,
) -> Callable[[ParamT1], ReturnT]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2], ReturnT],
    arity: None = ...,
) -> Callable[[ParamT2], Callable[[ParamT1], ReturnT]]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2, ParamT3], ReturnT],
    arity: None = ...,
) -> Callable[[ParamT3], Callable[[ParamT2], Callable[[ParamT1], ReturnT]]]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4], ReturnT],
    arity: None = ...,
) -> Callable[
    [ParamT4],
    Callable[[ParamT3], Callable[[ParamT2], Callable[[ParamT1], ReturnT]]],
]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5], ReturnT],
    arity: None = ...,
) -> Callable[
    [ParamT5],
    Callable[
        [ParamT4],
        Callable[[ParamT3], Callable[[ParamT2], Callable[[ParamT1], ReturnT]]],
    ],
]: ...
@overload
def curry_right(
    func: Callable[ArgKwargP, ReturnT],
    arity: Literal[1],
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamT1, ArgKwargP], ReturnT],
    arity: Literal[2],
) -> Callable[ArgKwargP, Callable[[ParamT1], ReturnT]]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamT1, ParamT2, ArgKwargP], ReturnT],
    arity: Literal[3],
) -> Callable[
    ArgKwargP,
    Callable[[ParamT2], Callable[[ParamT1], ReturnT]],
]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamT1, ParamT2, ParamT3, ArgKwargP], ReturnT],
    arity: Literal[4],
) -> Callable[
    ArgKwargP,
    Callable[
        [ParamT3],
        Callable[[ParamT2], Callable[[ParamT1], ReturnT]],
    ],
]: ...
@overload
def curry_right(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP],
        ReturnT,
    ],
    arity: Literal[5],
) -> Callable[
    ArgKwargP,
    Callable[
        [ParamT4],
        Callable[
            [ParamT3],
            Callable[
                [ParamT2],
                Callable[[ParamT1], ReturnT],
            ],
        ],
    ],
]: ...
@overload
def curry_right(
    func: Callable[ArgKwargP, ReturnT],
    arity: int | None = ...,
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> Callable[..., ReturnT]: ...
