from functools import _CacheInfo
from typing import Any, Callable, Generator, Generic, Iterable, final

from ..__generics import ArgKwargP, ParamT1, ParamT2, ReturnT
from ..dummies.obj import obejct_ as __initial_missing

__all__ = (
    "lru_cache",
    "reduce_generator",
)

def reduce_generator(
    func: Callable[[ParamT1, ParamT2], ParamT1],
    sequence: Iterable[ParamT2],
    initial: ParamT1 | object = __initial_missing,
) -> Generator[ParamT1, None, None]:
    """
    This is a modified version of functools.reduce that returns a generator.
    To get the last result of the function, consider to use:
    >>> *_, x = reduce_generator(...)

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
    ...

def lru_cache(
    maxsize: int | None = None,
) -> Callable[[Callable[ArgKwargP, ReturnT]], Callable[ArgKwargP, ReturnT]]:
    """
    Improved type hints of functools.lru_cache, for temporary use

    - See:
      https://github.com/python/mypy/issues/5107#issuecomment-1355954910
    """
    ...
@final
class _lru_cache_wrapper(Generic[ArgKwargP, ReturnT]):
    """
    Improved type hints of functools._lru_cache_wrapper, for temporary use

    - See:
      https://github.com/python/mypy/issues/5107#issuecomment-1355954910
    """

    def __call__(
        self, *args: ArgKwargP.args, **kwargs: ArgKwargP.kwargs
    ) -> ReturnT: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    def __copy__(self) -> _lru_cache_wrapper[ArgKwargP, ReturnT]: ...
    def __deepcopy__(self, __memo: Any) -> _lru_cache_wrapper[ArgKwargP, ReturnT]: ...
