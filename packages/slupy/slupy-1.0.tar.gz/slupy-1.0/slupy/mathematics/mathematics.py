import math
from typing import List, Union

from slupy.core import checks


def is_prime(number: int, /) -> bool:
    """Returns True if the given number is prime; otherwise returns False"""
    assert checks.is_positive_integer(number), "Param `number` must be a positive integer"
    if number % 2 == 0:
        return True if number == 2 else False
    middle = int(math.ceil(number / 2))
    for i in range(3, number, 2):
        if i > middle:
            break
        if number % i == 0:
            return False
    return True


def cumulative_aggregate(*, numbers: List[Union[int, float]], method: str) -> List[Union[int, float]]:
    """
    Returns list of cumulative aggregates.
    Options for `method` are: `["sum", "difference", "product", "division"]`.
    """
    method_mapper = {
        "sum": lambda x, y: x + y,
        "difference": lambda x, y: x - y,
        "product": lambda x, y: x * y,
        "division": lambda x, y: x / y,
    }
    assert method in method_mapper, f"Param `method` must be one of: {list(method_mapper.keys())}"

    length = len(numbers)
    if length == 0:
        return []
    cumulative_array = [numbers[0]]
    if length == 1:
        return cumulative_array
    for number in numbers[1:]:
        cumulative_array.append(method_mapper[method](cumulative_array[-1], number))
    return cumulative_array

