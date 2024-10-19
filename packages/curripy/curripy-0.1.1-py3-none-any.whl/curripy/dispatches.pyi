from re import Pattern
from typing import AnyStr, overload

@overload
def split(instance: str) -> list[str]: ...
@overload
def split(instance: Pattern[AnyStr]) -> list[AnyStr]: ... 