import re
import string
from typing import List, Optional

from slupy.core import checks


DIGITS = set(string.digits)
ALPHABETS_LOWER_CASED = set(string.ascii_lowercase)
ALPHABETS_UPPER_CASED = set(string.ascii_uppercase)
ALPHABETS = ALPHABETS_LOWER_CASED.union(ALPHABETS_UPPER_CASED)
ALPHABETS_AND_DIGITS = ALPHABETS.union(DIGITS)
CHARSET_LOWER_SNAKE_CASE = ALPHABETS_LOWER_CASED.union(DIGITS).union(["_"])
CHARSET_UPPER_SNAKE_CASE = ALPHABETS_UPPER_CASED.union(DIGITS).union(["_"])
CHARSET_LOWER_KEBAB_CASE = ALPHABETS_LOWER_CASED.union(DIGITS).union(["-"])
CHARSET_UPPER_KEBAB_CASE = ALPHABETS_UPPER_CASED.union(DIGITS).union(["-"])


def make_message(
        message: str,
        /,
        *,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        sep: Optional[str] = None,
    ) -> str:
    """Helps construct a message with a `prefix` and a `suffix` (separated by the `sep`)"""
    sep = "" if sep is None else sep
    components = []
    if prefix:
        components.append(prefix)
    components.append(message)
    if suffix:
        components.append(suffix)
    return f"{sep}".join(components)


def is_part_of_charset(*, text: str, charset: set[str]) -> bool:
    """Checks if the given `text` is part of the given `charset`"""
    assert isinstance(text, str) and bool(text), "Param `text` must be a non-empty string"
    assert isinstance(charset, set) and bool(charset), "Param `charset` must be a non-empty set of strings"
    return all((char in charset for char in text))


def is_snake_case(s: str, /, *, as_uppercase: Optional[bool] = False) -> bool:
    charset = CHARSET_UPPER_SNAKE_CASE if as_uppercase else CHARSET_LOWER_SNAKE_CASE
    return (
        bool(s)
        and is_part_of_charset(text=s, charset=charset)
        and not s[0].isdigit()
        and not s.startswith("_")
        and not s.endswith("_")
        and "__" not in s  # cannot have successive underscores
    )


def is_kebab_case(s: str, /, *, as_uppercase: Optional[bool] = False) -> bool:
    charset = CHARSET_UPPER_KEBAB_CASE if as_uppercase else CHARSET_LOWER_KEBAB_CASE
    return (
        bool(s)
        and is_part_of_charset(text=s, charset=charset)
        and not s[0].isdigit()
        and not s.startswith("-")
        and not s.endswith("-")
        and "--" not in s  # cannot have successive hyphens
    )


def is_camel_case(s: str, /) -> bool:
    return (
        bool(s)
        and is_part_of_charset(text=s, charset=ALPHABETS_AND_DIGITS)
        and s[0].islower()
        and not s[0].isdigit()
    )


def is_pascal_case(s: str, /) -> bool:
    return (
        bool(s)
        and is_part_of_charset(text=s, charset=ALPHABETS_AND_DIGITS)
        and s[0].isupper()
        and not s[0].isdigit()
    )


def camel_to_pascal(string: str, /) -> str:
    """
    Converts camel-case to pascal-case.
    >>> camel_to_pascal("helloAndGoodMorning") # Returns "HelloAndGoodMorning"
    """
    assert is_camel_case(string), "Given string is not in camel case"
    return string[0].upper() + string[1:]


def camel_to_snake(string: str, /) -> str:
    """
    Converts camel-case to snake-case.
    >>> camel_to_snake("helloAndGoodMorning") # Returns "hello_and_good_morning"
    """
    assert is_camel_case(string), "Given string is not in camel case"
    string_in_pascal = camel_to_pascal(string)
    string_in_snake = pascal_to_snake(string_in_pascal)
    return string_in_snake


def pascal_to_camel(string: str, /) -> str:
    """
    Converts pascal-case to camel-case.
    >>> pascal_to_camel("HelloAndGoodMorning") # Returns "helloAndGoodMorning"
    """
    assert is_pascal_case(string), "Given string is not in pascal case"
    return string[0].lower() + string[1:]


def pascal_to_snake(string: str, /) -> str:
    """
    Converts pascal-case to snake-case.
    >>> pascal_to_snake("HelloAndGoodMorning") # Returns "hello_and_good_morning"
    """
    assert is_pascal_case(string), "Given string is not in pascal case"
    words = re.findall(pattern="[A-Z][^A-Z]*", string=string)
    words_lower_cased = list(map(str.lower, words))
    return "_".join(words_lower_cased)


def snake_to_pascal(string: str, /) -> str:
    """
    Converts snake-case to pascal-case.
    >>> snake_to_pascal("hello_and_good_morning") # Returns "HelloAndGoodMorning"
    """
    assert is_snake_case(string), "Given string is not in snake case"
    words = string.split('_')
    words_capitalized = list(map(str.capitalize, words))
    return "".join(words_capitalized)


def snake_to_camel(string: str, /) -> str:
    """
    Converts snake-case to camel-case.
    >>> snake_to_camel("hello_and_good_morning") # Returns "helloAndGoodMorning"
    """
    assert is_snake_case(string), "Given string is not in snake case"
    string_in_pascal = snake_to_pascal(string)
    string_in_camel = pascal_to_camel(string_in_pascal)
    return string_in_camel


def snake_to_kebab(string: str, /) -> str:
    """
    Converts snake-case to kebab-case.
    >>> snake_to_kebab("hello_and_good_morning") # Returns "hello-and-good-morning"
    """
    assert is_snake_case(string), "Given string is not in snake case"
    return string.replace("_", "-")


def kebab_to_snake(string: str, /) -> str:
    """
    Converts kebab-case to snake-case.
    >>> kebab_to_snake("hello-and-good-morning") # Returns "hello_and_good_morning"
    """
    assert is_kebab_case(string), "Given string is not in kebab case"
    return string.replace("-", "_")


def to_dumbo_text(s: str, /) -> str:
    """
    Converts given text to retardified text.
    >>> to_dumbo_text("Hello, and good morning!") # Returns "hElLo, AnD gOoD mOrNiNg!"
    """
    counter = 0
    result_text = ""
    for character in s.lower():
        if character in ALPHABETS:
            counter += 1
            if counter % 2 == 0:
                character = character.upper()
        result_text += character
    return result_text


def get_first_n_characters(*, text: str, num_chars: int) -> str:
    assert checks.is_positive_integer(num_chars), "Param `num_chars` must be a positive integer"
    return text[:num_chars]


def get_last_n_characters(*, text: str, num_chars: int) -> str:
    assert checks.is_positive_integer(num_chars), "Param `num_chars` must be a positive integer"
    return text[-num_chars:]


def remove_first_n_characters(*, text: str, num_chars: int) -> str:
    assert checks.is_positive_integer(num_chars), "Param `num_chars` must be a positive integer"
    return text[num_chars:]


def remove_last_n_characters(*, text: str, num_chars: int) -> str:
    assert checks.is_positive_integer(num_chars), "Param `num_chars` must be a positive integer"
    return text[:-num_chars]


def remove_characters_at_indices(*, text: str, indices: List[int]) -> str:
    """
    Removes characters present at the given `indices` in the `text`.
    Expects `indices` to be in range (0, n-1) where n is the length of the `text`.
    Raises an IndexError if any of the given `indices` are out of bounds.
    """
    if not indices:
        return text
    indices = sorted(list(set(indices)), reverse=True)
    lowest_possible_index, highest_possible_index = 0, len(text) - 1 # Must not use negative indices
    if indices[-1] < lowest_possible_index or indices[0] > highest_possible_index:
        raise IndexError(
            f"Accepted index-range for the given text is ({lowest_possible_index}, {highest_possible_index})."
            f" i.e; position-range ({lowest_possible_index + 1}, {highest_possible_index + 1})."
            " Cannot remove character at an index/position outside of this range."
        )
    chars = list(text)
    for index in indices:
        chars.pop(index)
    return "".join(chars)


def remove_characters_at_positions(*, text: str, positions: List[int]) -> str:
    """
    Removes characters present at the given `positions` in the `text`.
    Expects `positions` to be in range (1, n) where n is the length of the `text`.
    Raises an IndexError if any of the given `positions` are out of bounds.
    """
    return remove_characters_at_indices(text=text, indices=[position - 1 for position in positions])

