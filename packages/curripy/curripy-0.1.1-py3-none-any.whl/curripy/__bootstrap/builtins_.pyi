from _collections_abc import ValuesView
from typing import (
    Any,
    Callable,
    ItemsView,
    Iterable,
    KeysView,
    Mapping,
    TypeVar,
    overload,
)

from typing_extensions import TypeIs

from curripy.utils.curry_ import curry

from ..__generics import (
    ParamT,
    ParamT1,
    ParamT2,
    ParamT3,
    ParamT4,
    ParamT5,
    ReturnT,
)

__all__ = (
    "filter_",
    "map_",
    "values",
    "keys",
)

KeyType = TypeVar("KeyType")
ValueType = TypeVar("ValueType")

# filter_  = curry(filter)
map_ = curry(map)

@overload
def filter_(
    func: Callable[[ParamT1], TypeIs[ParamT2]],
) -> Callable[[Iterable[ParamT1]], filter[ParamT2]]: ...
@overload
def filter_(
    func: Callable[[ParamT], Any],
) -> Callable[[Iterable[ParamT]], filter[Any]]: ...
@overload
def filter_(
    func: None,
) -> Callable[[Iterable[ParamT | None]], filter[ParamT]]: ...

# @overload
# def map_(
#     func: Callable[[ParamT1], ReturnT],
# ) -> Callable[
#     [Iterable[ParamT1]],
#     map[ReturnT],
# ]: ...
# @overload
# def map_(
#     func: Callable[[ParamT1, ParamT2], ReturnT],
# ) -> Callable[
#     [Iterable[ParamT1], Iterable[ParamT2]],
#     map[ReturnT],
# ]: ...
# @overload
# def map_(
#     func: Callable[[ParamT1, ParamT2, ParamT3], ReturnT],
# ) -> Callable[
#     [
#         Iterable[ParamT1],
#         Iterable[ParamT2],
#         Iterable[ParamT3],
#     ],
#     map[ReturnT],
# ]: ...
# @overload
# def map_(
#     func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4], ReturnT],
# ) -> Callable[
#     [
#         Iterable[ParamT1],
#         Iterable[ParamT2],
#         Iterable[ParamT3],
#         Iterable[ParamT4],
#     ],
#     map[ReturnT],
# ]: ...
# @overload
# def map_(
#     func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5], ReturnT],
# ) -> Callable[
#     [
#         Iterable[ParamT1],
#         Iterable[ParamT2],
#         Iterable[ParamT3],
#         Iterable[ParamT4],
#         Iterable[ParamT5],
#     ],
#     map[ReturnT],
# ]: ...
def values(d: Mapping[KeyType, ValueType]) -> ValuesView[ValueType]: ...
def items(d: Mapping[KeyType, ValueType]) -> ItemsView[KeyType, ValueType]: ...
def keys(d: Mapping[KeyType, ValueType]) -> KeysView[KeyType]: ...
