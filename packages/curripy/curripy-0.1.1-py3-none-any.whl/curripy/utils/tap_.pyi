from typing import Callable
from ..__generics import ParamT

def tap(
    func: Callable[[ParamT], None],
) -> Callable[[ParamT], ParamT]: ...
