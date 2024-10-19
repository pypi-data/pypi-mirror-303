import re
from ..utils import curry

__all__ = ()

# functions not exported to root package
findall = curry(re.findall)
finditer = curry(re.finditer)
fullmatch = curry(re.fullmatch)
match_ = curry(re.match)
search = curry(re.search)
sub = curry(re.sub)
subn = curry(re.subn)
