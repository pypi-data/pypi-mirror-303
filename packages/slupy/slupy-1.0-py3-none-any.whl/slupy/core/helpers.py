import copy
import math
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from slupy.core import checks

Sliceable = Union[list, tuple, str]


def make_deep_copy(obj: Any, /) -> Any:
    """Returns deep-copy of the given object"""
    return copy.deepcopy(obj)


def make_shallow_copy(obj: Any, /) -> Any:
    """Returns shallow-copy of the given object"""
    return copy.copy(obj)


def slice_by_position(
        sliceable: Sliceable,
        /,
        *,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> Sliceable:
    """
    Slice the given sliceable object by position (not by index).
    The position can range from 1-n (where `n` is the length of the sliceable).
    """
    if start is None and end is None:
        return sliceable[:]
    if start is not None and end is None:
        assert start >= 1, "Position `start` must be >= 1"
        return sliceable[start - 1 : ]
    if start is None and end is not None:
        assert end >= 1, "Position `end` must be >= 1"
        return sliceable[ : end]
    assert end >= start >= 1, "Position `end` must be >= `start`; and `start` must be >= 1"
    return sliceable[start - 1 : end]


def compute_partitions(
        *,
        length: int,
        zero_based: Optional[bool] = True,
        num_partitions: Optional[int] = None,
        partition_size: Optional[int] = None,
    ) -> List[Tuple[int, int]]:
    """
    Returns list of tuples having (start, end) indices.

    Parameters:
        - length (int): Length of the data to be partitioned.
        - zero_based (bool): Indexing type of the partitions. If `zero_based=True`, will be 0-based; otherwise will be 1-based.
        - num_partitions (int): Number of partitions.
        - partition_size (int): Size of each partition.
    """
    assert length >= 1, "Param `length` must be >= 1"
    assert isinstance(zero_based, bool), "Param `zero_based` must be of type 'bool'"
    assert num_partitions is None or num_partitions >= 1, "Param `num_partitions` must be >= 1"
    assert partition_size is None or partition_size >= 1, "Param `partition_size` must be >= 1"
    assert sum([
        num_partitions is not None,
        partition_size is not None,
    ]) == 1, "Expected exactly one of the following params: ['num_partitions', 'partition_size']"
    if num_partitions is not None:
        partition_size = math.ceil(length / num_partitions)
    partitions = []
    for i in range(1, length + 1, partition_size):
        start = i
        end = i + partition_size - 1
        if end > length:
            end = length
        if zero_based:
            start -= 1
            end -= 1
        partitions.append((start, end))
    return partitions


def _get_kwarg_as_string(key: Any, value: Any) -> str:
    return f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}"


def _single_line_repr(
        *,
        class_name: str,
        kwargs_dict: Dict[str, Any],
    ) -> str:
    if not kwargs_dict:
        return f"{class_name}()"
    kwargs_dict_as_string = ", ".join(
        [_get_kwarg_as_string(key=key, value=value) for key, value in kwargs_dict.items()]
    )
    return f"{class_name}({kwargs_dict_as_string})"


def _multi_line_repr(
        *,
        class_name: str,
        kwargs_dict: Dict[str, Any],
    ) -> str:
    if not kwargs_dict:
        return f"{class_name}()"
    indent = 4
    kwargs_dict_as_string = ""
    for key, value in kwargs_dict.items():
        kwargs_dict_as_string += " " * indent + _get_kwarg_as_string(key=key, value=value) + "," + "\n"
    kwargs_dict_as_string = kwargs_dict_as_string.rstrip()
    return f"{class_name}(\n{kwargs_dict_as_string}\n)"


def create_repr(
        *,
        instance: Any,
        kwargs_dict: Optional[Dict[str, Any]] = None,
        multi_line: Optional[bool] = True,
    ) -> str:
    """
    Returns a representation of a class' instance.

    ```
    class Person:
        pass

    >>> create_repr(
        instance=Person(),
        kwargs_dict={
            "first_name": "James",
            "last_name": "Murphy",
            "age": 35,
            "is_developer": True,
        },
        multi_line=False,
    ) # Returns the string: "Person(first_name='James', last_name='Murphy', age=35, is_developer=True)"
    ```
    """
    assert kwargs_dict is None or isinstance(kwargs_dict, dict), f"Param `kwargs_dict` must be of type 'dict'"
    kwargs_dict = kwargs_dict or {}
    kw = {
        "class_name": instance.__class__.__name__,
        "kwargs_dict": kwargs_dict,
    }
    return _multi_line_repr(**kw) if multi_line else _single_line_repr(**kw)


def print_docstring(obj: Any) -> None:
    """Prints the doc-string (if available). Usually of a class, method or function."""
    if hasattr(obj, "__doc__"):
        print(obj.__doc__)


def rename_dict_keys(
        dict_: Dict[str, Any],
        /,
        *,
        update_func: Callable[[str], str],
        deep: Optional[bool] = False,
    ) -> Dict[str, Any]:
    """
    Renames the keys of the given dictionary, based on the given `update_func`.
    Returns a new dictionary having the updated keys. The original dictionary will remain unchanged.

    Parameters:
        - dict_: The dictionary.
        - update_func (Callable): The function that takes in the current key and returns the new key.
        - deep (bool): If `deep=True`, it also renames the dictionary keys of all the nested dictionaries.
    """
    assert checks.is_valid_object_of_type(dict_, type_=dict, allow_empty=False), (
        "Param `dict_` must be of type 'dict' and must be non-empty"
    )
    return _rename_dict_keys(
        dict_original=dict_,
        dict_copy=make_deep_copy(dict_),
        update_func=update_func,
        deep=deep,
    )


def _rename_dict_keys(
        *,
        dict_original: Dict[str, Any],
        dict_copy: Dict[str, Any],
        update_func: Callable[[str], str],
        deep: Optional[bool] = False,
    ) -> Dict[str, Any]:
    for key in dict_original:
        new_key = update_func(key)
        if new_key != key and new_key in dict_original:
            raise ValueError(
                " || ".join([
                    "The new key obtained from the `update_func` is already present in the given dictionary",
                    f"New key: `{new_key}`",
                    f"Keys present in dictionary: `{list(dict_original.keys())}`",
                ])
            )
        dict_copy[new_key] = dict_copy.pop(key)

        if not deep:
            continue

        value_original = dict_original[key]
        value_copy = dict_copy[new_key]

        if isinstance(value_copy, dict):
            value_copy = _rename_dict_keys(
                dict_original=value_original,
                dict_copy=value_copy,
                update_func=update_func,
                deep=deep,
            )
            dict_copy[new_key] = value_copy
        elif isinstance(value_copy, (list, tuple)):
            class_type = type(value_copy)
            value_copy = value_copy if class_type is list else list(value_copy)  # convert to list as it's mutable
            for idx, item in enumerate(value_copy):
                if isinstance(item, dict):
                    item = _rename_dict_keys(
                        dict_original=value_original[idx],
                        dict_copy=item,
                        update_func=update_func,
                        deep=deep,
                    )
                    value_copy[idx] = item
                    dict_copy[new_key] = value_copy if class_type is list else class_type(value_copy)  # convert back to original `class_type`

    return dict_copy
