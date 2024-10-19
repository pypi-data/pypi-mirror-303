from .tap_ import tap


@tap
def raise_(error):
    raise error
