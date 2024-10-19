from ..__bootstrap.inspect_ import len_of_regular_args
from ..__bootstrap.operator_ import or_, radd, add

__all__ = (
    "curry",
    "curry_right",
)


def __init_args(
    recursion,
    arity: int | None = None,
):
    def caller(func, *args, **kwargs):
        nonlocal arity
        init_args = () if args is None else args
        init_kwargs = {} if kwargs is None else kwargs
        init_arity = len_of_regular_args(func) if arity is None else arity
        return recursion(func, init_arity, *init_args, **init_kwargs)

    return caller


def __merge_args(
    recursion,
    func,
    arity,
    process_args,
    process_kwargs,
    args,
    kwargs,
):
    def caller(*passing_args, **passing_kwargs):
        return recursion(
            func,
            arity,
            *process_args(args)(passing_args),
            **process_kwargs(kwargs)(passing_kwargs),
        )

    return caller


def __define_order(process_args, process_kwargs=or_):
    def portal(
        func=None,
        arity: int | None = None,
        *args,
        **kwargs,
    ):
        """
        This function gets arguments recursively, and call the passed function after being received enough positional arguments which have the same amount of the arity.
        Currently any keywords arguments will be overwritten by keywords newly passed in any generation of curried function.

        Args:
            func (Callable[ArgumentType, ReturnT]): the function to be curried.
            arity (int | None, optional): max number of arguments to be passed. Defaults to None.

        Returns:
            Callable | ReturnT: a partial applied function or final return of the function
        """
        nonlocal process_args, process_kwargs
        __self = portal
        decorator = __init_args(
            __self,
            arity,
        )

        if func is None:
            # As a decorator to receive a Callable
            return decorator
        if arity is None:
            # Func getted. Determining length of paratmeters
            init_arity = decorator(func=func, *args, **kwargs)
            return init_arity
        elif len(args) >= arity:
            # Received enough parameters, call the func
            return func(*args, **kwargs)
        elif arity > 1:
            return __merge_args(
                __self,
                func,
                arity,
                process_args=process_args,
                process_kwargs=process_kwargs,
                args=args,
                kwargs=kwargs,
            )
        return func

    return portal


curry = __define_order(add)
curry_right = __define_order(radd)
