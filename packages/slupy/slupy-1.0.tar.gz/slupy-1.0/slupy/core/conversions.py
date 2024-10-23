from typing import List, Union


def integerify_if_possible(number: Union[int, float], /) -> Union[int, float]:
    """Converts whole numbers represented as floats to integers"""
    number_as_int = int(number)
    return number_as_int if number_as_int == number else number


def round_off_as_string(*, number: Union[int, float], round_by: int) -> str:
    """
    Rounds off the given `number` to `round_by` decimal places, and type casts
    it to a string (to retain the exact number of decimal places desired).
    """
    if round_by < 0:
        raise ValueError("The `round_by` parameter must be >= 0")
    if round_by == 0:
        return str(round(number))
    number_stringified = str(round(number, round_by))
    decimal_places_filled = len(number_stringified.split('.')[-1])
    decimal_places_to_fill = round_by - decimal_places_filled
    for _ in range(decimal_places_to_fill):
        number_stringified += '0'
    return number_stringified


def commafy_number(number: Union[int, float], /) -> str:
    """
    Adds commas to number for better readability.

    ```
    >>> commafy_number(1738183090) # Returns "1,738,183,090"
    >>> commafy_number(1738183090.90406) # Returns "1,738,183,090.90406"
    ```
    """
    if int(number) == number:
        return format(int(number), ",d")
    return format(number, ",f")


def string_to_int_or_float(value: str, /) -> Union[int, float]:
    """Converts stringified number to either int or float"""
    number = float(value)
    number = integerify_if_possible(number)
    return number


def stringify_list_of_nums(array: List[Union[int, float]], /) -> str:
    """Converts list of ints/floats to comma separated string of the same"""
    return ",".join(list(map(str, array)))


def listify_string_of_nums(s: str, /) -> List[Union[int, float]]:
    """Converts string of comma separated ints/floats to list of numbers"""
    numbers = s.split(",")
    numbers = list(map(string_to_int_or_float, numbers))
    return numbers

