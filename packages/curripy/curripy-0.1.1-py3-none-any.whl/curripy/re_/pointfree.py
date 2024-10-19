import re
from ..utils import curry_right

__all__ = (
    "findall",
    "finditer",
    "fullmatch",
    "match_",
    "search",
    "sub",
    "subn",
)

findall = curry_right(re.findall)
finditer = curry_right(re.finditer)
fullmatch = curry_right(re.fullmatch)
match_ = curry_right(re.match)
search = curry_right(re.search)
sub = curry_right(re.sub)
subn = curry_right(re.subn)
