import sys
from types import UnionType
from typing import TypeAlias

if sys.version_info >= (3, 10):
    _ClassInfo: TypeAlias = type | UnionType | tuple[_ClassInfo, ...]
    """a simulated type to the one with the same name in builtins.pyi"""
else:
    _ClassInfo: TypeAlias = type | tuple[_ClassInfo, ...]
