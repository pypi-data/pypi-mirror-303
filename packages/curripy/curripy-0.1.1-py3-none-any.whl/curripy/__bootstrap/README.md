# __bootstrap

This package contains some manual-curried functions that are needed before defining functions in ``utils`` like ``partial`` and ``curry``.

In other words, functions in ``utils``should **never** be used in this package to prevent errors from circular imports.
