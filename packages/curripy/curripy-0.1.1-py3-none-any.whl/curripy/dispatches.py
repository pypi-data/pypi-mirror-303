from functools import singledispatch
import sys
from typing import AnyStr, SupportsAbs

from curripy.protocols import SupportsSplit


@singledispatch
def split(instance: SupportsSplit):
    return instance.split


@split.register(str)
def __str_split(instance: str):
    return instance.split

if "re" in sys.modules:
    from re import Pattern

    @split.register(Pattern[str])
    def __pattern_str_split(instance: Pattern[AnyStr]):
        return instance.split
