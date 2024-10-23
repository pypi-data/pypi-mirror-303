from functools import cmp_to_key
from operator import itemgetter
from typing import Any, List


def cmp(x: Any, y: Any) -> int:
    """
    Replacement for built-in function cmp that was removed in Python 3.

    Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == y
    and strictly positive if x > y.

    Reference: https://portingguide.readthedocs.io/en/latest/comparisons.html#the-cmp-function
    """
    if x is None and y is None:
        return 0
    if x is None and y is not None:
        return -1
    if x is not None and y is None:
        return 1
    return (x > y) - (x < y)


def multi_key_sort(
        iterable: List[Any],
        /,
        *,
        columns: List[str],
        ascending: List[bool],
    ) -> List[Any]:
    """Returns a new list with the sorted iterable"""
    comparers = [
        (
            (itemgetter(column), 1)
            if ascending_ else
            (itemgetter(column), -1)
        )
        for column, ascending_ in zip(columns, ascending)
    ]

    def comparer(left: Any, right: Any) -> int:
        comparer_iter = (
            cmp(fn(left), fn(right)) * mult
            for fn, mult in comparers
        )
        return next((result for result in comparer_iter if result), 0)

    return sorted(
        iterable,
        key=cmp_to_key(comparer),
    )

