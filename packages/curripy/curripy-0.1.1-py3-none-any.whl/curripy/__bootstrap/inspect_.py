from inspect import Parameter, Signature, signature
from operator import not_

from ..__overlays.functools_ import lru_cache
from .builtins_ import filter_, values
from .compose_ import compose, pipe
from .operator_ import contains, is_


__all__ = ("signature_parameters", "get_regular_args")


def get_parameters(sig: Signature):
    return sig.parameters


def get_default(obj: Parameter):
    return obj.default


def get_name(obj: Parameter):
    return obj.name


# base function
signature_parameters = lru_cache()(pipe(signature, get_parameters))
"""Get parameters from the signature of the function"""

# get Parameter of args and kwargs
not_contains_asterisk = compose(not_, contains("*"))
not_var_args = pipe(get_name, not_contains_asterisk)
"""Check if a argument is *args or **kwargs"""

is_empty = is_(Signature.empty)
not_have_default = pipe(get_default, is_empty)
"""Check if a parameter has a default value"""

filter_out_var_args = filter_(not_var_args)
filter_out_optional_args = filter_(not_have_default)

all_params = pipe(signature_parameters, values)
get_regular_args = lru_cache()(
    pipe(
        all_params,
        filter_out_var_args,
        filter_out_optional_args,
        tuple,
    )
)
len_of_args = pipe(signature_parameters, len)
len_of_regular_args = pipe(get_regular_args, len)
