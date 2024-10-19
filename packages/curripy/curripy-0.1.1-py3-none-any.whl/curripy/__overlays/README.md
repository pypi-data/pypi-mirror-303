# __overlays

This private package is only used for storing  ``.pyi``(stub files) for better type hint support,
and contains some reinvented wheels which is for implementing the ones of standard library in more pure & typed ways.

Related contents would be **removed** if upstream had offered better solutions.

## List of  functions whose type hints got overlaid

### operator

- add
- contains
- sub
- is_
- is_not
- getitem

### functools

- lru_cache
- singledispatch

## List of functions used for extending stdlib

### extensions for operator

- radd
- rsub
