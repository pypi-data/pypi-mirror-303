from typing import Any, Dict, List, Optional, Type, Union


def dict_has_any_keys(d: Dict, /, *, keys: List) -> bool:
    return any((key in keys for key in d))


def dict_has_all_keys(d: Dict, /, *, keys: List) -> bool:
    return all((key in keys for key in d))


def is_instance_of_any(obj: Any, /, *, types: List[Type]) -> bool:
    return isinstance(obj, tuple(types))


def is_collection_of_items(obj: Any, /) -> bool:
    """If the given `obj` is one of `[list, tuple, set]`, returns `True`"""
    return is_instance_of_any(obj, types=[list, tuple, set])


def is_list_of_instances_of_type(obj: Any, /, *, type_: Type, allow_empty: Optional[bool] = True) -> bool:
    """Returns True if `obj` is a list of instances of type `type_`"""
    if not isinstance(obj, list):
        return False
    if not allow_empty and not obj:
        return False
    return all((isinstance(item, type_) for item in obj))


def is_list_of_subclasses_of_type(obj: Any, /, *, type_: Type, allow_empty: Optional[bool] = True) -> bool:
    """Returns True if `obj` is a list of sub-classes of type `type_`"""
    if not isinstance(obj, list):
        return False
    if not allow_empty and not obj:
        return False
    return all((bool(isinstance(item, type) and issubclass(item, type_)) for item in obj))


def is_valid_object_of_type(obj: Any, /, *, type_: Type, allow_empty: Optional[bool] = True) -> bool:
    if not isinstance(obj, type_):
        return False
    return True if allow_empty else bool(obj)


def is_zero_or_none(x: Any, /) -> bool:
    return x == 0 or x is None


def is_boolean(x: Any, /) -> bool:
    return isinstance(x, bool)


def is_integer(x: Any, /) -> bool:
    return isinstance(x, int)


def is_number(x: Any, /) -> bool:
    return isinstance(x, (int, float))


def is_positive_integer(x: Any, /) -> bool:
    return is_integer(x) and x > 0


def is_positive_number(x: Any, /) -> bool:
    return is_number(x) and x > 0


def is_non_negative_integer(x: Any, /) -> bool:
    return is_integer(x) and x >= 0


def is_non_negative_number(x: Any, /) -> bool:
    return is_number(x) and x >= 0


def list_has_negative_number(array: List[Union[int, float]], /) -> bool:
    return any((number < 0 for number in array))


def list_has_non_negative_number(array: List[Union[int, float]], /) -> bool:
    return any((number >= 0 for number in array))


def list_has_positive_number(array: List[Union[int, float]], /) -> bool:
    return any((number > 0 for number in array))

