from typing import Any, Awaitable, Iterable, Protocol, Self
from .__generics import ArgKwargP, ParamTCon, ReturnTCov


class SupportsContains(Protocol):
    def __contains__(self, x: Any, /) -> bool: ...


class SupportsGetItem(Protocol[ParamTCon, ReturnTCov]):
    def __getitem__(self, x: ParamTCon, /) -> ReturnTCov: ...


class SupportsRShift(Protocol[ParamTCon, ReturnTCov]):
    def __rshift__(self, x: ParamTCon, /) -> ReturnTCov: ...


class SupportsLShift(Protocol[ParamTCon, ReturnTCov]):
    def __lshift__(self, x: ParamTCon, /) -> ReturnTCov: ...


class SupportsNext(Protocol[ReturnTCov]):
    def __next__(self) -> ReturnTCov: ...


class SupportsAnext(Protocol[ReturnTCov]):
    def __anext__(self) -> Awaitable[ReturnTCov]: ...


#  protocols
class SupportsAdd(Protocol[ParamTCon, ReturnTCov]):
    def __add__(self, x: ParamTCon, /) -> ReturnTCov: ...


# FIXME not compatible with any type
# joke: SupportsOr or not supported
class SupportsOr(Protocol[ParamTCon, ReturnTCov]):
    def __or__(self, x: ParamTCon) -> ReturnTCov: ...


class SupportsRAdd(Protocol[ParamTCon, ReturnTCov]):
    def __radd__(self, x: ParamTCon, /) -> ReturnTCov: ...


class SupportsSub(Protocol[ParamTCon, ReturnTCov]):
    def __sub__(self, x: ParamTCon, /) -> ReturnTCov: ...


class SupportsRSub(Protocol[ParamTCon, ReturnTCov]):
    def __rsub__(self, x: ParamTCon, /) -> ReturnTCov: ...


class SupportsDivMod(Protocol[ParamTCon, ReturnTCov]):
    def __divmod__(self, other: ParamTCon, /) -> ReturnTCov: ...


class SupportsRDivMod(Protocol[ParamTCon, ReturnTCov]):
    def __rdivmod__(self, other: ParamTCon, /) -> ReturnTCov: ...


class SupportsLT(Protocol[ParamTCon]):
    def __lt__(self, other: ParamTCon, /) -> bool: ...


class SupportsGT(Protocol[ParamTCon]):
    def __gt__(self, other: ParamTCon, /) -> bool: ...


class SupportsLE(Protocol[ParamTCon]):
    def __le__(self, other: ParamTCon, /) -> bool: ...


class SupportsGE(Protocol[ParamTCon]):
    def __ge__(self, other: ParamTCon, /) -> bool: ...


class SupportsIter(Protocol[ReturnTCov]):
    def __iter__(self) -> ReturnTCov: ...


class SupportsTrunc(Protocol):
    def __trunc__(self) -> int: ...


# composed protocols
class SupportsContainsAndGetItem(
    SupportsContains, SupportsGetItem[ParamTCon, ReturnTCov]
): ...


class SupportsAllComparisons(
    SupportsLT[Any],
    SupportsGT[Any],
    SupportsLE[Any],
    SupportsGE[Any],
    Protocol,
): ...


# protocols of non-dunder methods
class SupportsSplit(Protocol):
    def split(self, *args, **kwargs) -> Iterable: ...
