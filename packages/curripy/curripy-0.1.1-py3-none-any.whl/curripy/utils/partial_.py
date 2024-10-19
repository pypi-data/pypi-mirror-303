from ..__bootstrap.operator_ import or_, add, radd

__all__ = (
    "partial",
    "partial_right",
)


def __init_order(process_args, process_kwargs=or_):
    def portal(func, *args, **kwargs):
        def caller(*passing_args, **passing_kwargs):
            nonlocal process_args, process_kwargs, args, kwargs, func
            apply_args = process_args(args)(passing_args)
            apply_kwargs = process_kwargs(kwargs)(passing_kwargs)
            return func(*apply_args, **apply_kwargs)

        return caller

    return portal


partial = __init_order(add)
partial_right = __init_order(radd)
