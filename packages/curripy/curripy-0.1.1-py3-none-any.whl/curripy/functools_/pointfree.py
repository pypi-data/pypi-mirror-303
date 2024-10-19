from operator import attrgetter

__all__ = (
    "get_func",
    "get_args",
    "get_keywords",
)

get_func = attrgetter("func")
get_args = attrgetter("args")
get_keywords = attrgetter("keywords")
