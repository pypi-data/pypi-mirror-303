__all__ = (
    "def_kwargs",
    "def_args",
    "def_args_kwargs",
    "return_true",
    "return_false",
    "return_0",
    "return_1",
)


def def_args_kwargs(*args, **kwargs): ...
def def_kwargs(**kwargs): ...
def def_args(*args): ...


def return_true(_):
    return True


def return_false(_):
    return False


def return_0(_):
    return 0


def return_1(_):
    return 1
