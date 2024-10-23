from __future__ import annotations

from collections import Counter
from pprint import pprint
from typing import Any, Callable, Dict, List, Literal, Optional, Type

from slupy.core import checks
from slupy.core.helpers import make_deep_copy
from slupy.data_wrangler.utils import multi_key_sort


class Dataset:
    """Class that represents a dataset (collection of data as a list of dictionaries)"""

    def __init__(
            self,
            data: List[Dict[str, Any]],
            /,
            *,
            deep_copy: Optional[bool] = False,
            autofill: Optional[bool] = False,
        ) -> None:
        """
        Parameters:
            - data (list): List of dictionaries.
            - deep_copy (bool): If `deep_copy=True`, creates a deep-copy of the given `data` and
            ensures that the original is never modified.
            - autofill (bool): If `autofill=True`, checks if the existing unique fields are present in each dictionary
            in the list. If not present, sets their default value to `None`. Does this operation inplace.
        """
        assert checks.is_list_of_instances_of_type(data, type_=dict, allow_empty=True), (
            "Param `data` must be a list of dictionaries"
        )
        self._data = make_deep_copy(data) if deep_copy else data
        if autofill:
            self = self.autofill_missing_fields(inplace=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        return self.data[idx]

    def copy(self) -> Dataset:
        """Returns deep-copy of `self`"""
        return make_deep_copy(self)

    @property
    def data(self) -> List[Dict[str, Any]]:
        return self._data

    @data.setter
    def data(self, value: List[Dict[str, Any]]) -> None:
        assert checks.is_list_of_instances_of_type(value, type_=dict, allow_empty=True), (
            "Param `data` must be a list of dictionaries"
        )
        self._data = value

    def data_copy(self) -> List[Dict[str, Any]]:
        """Returns deep-copy of `self.data`"""
        return make_deep_copy(self.data)

    def _identify_duplicate_indices(
            self,
            *,
            break_at: Optional[Literal["first", "first_full"]] = None,
            subset: Optional[List[str]] = None,
        ) -> List[List[int]]:
        """
        Returns list of list of indices that correspond to duplicates. If no duplicates are found, returns an empty list.
        Eg: An output of `[[0, 4, 5], [1, 6, 8]]` means that dictionaries at indices (0, 4, 5) are duplicates of the same
        value; and dictionaries at indices (1, 6, 8) are duplicates of the same value.

        Parameters:
            - break_at (str): If `break_at='first'`, returns early with the first 2 indices of the first set of duplicates identified (if any).
            If `break_at='first_full'`, returns early with all the indices of the first set of duplicates identified (if any).
            - subset (List[str]): List of keys to consider in each dictionary in the list.
        """
        indices = []
        indices_involved_in_duplicates = set()
        for idx, dict_obj in enumerate(self.data):
            if idx in indices_involved_in_duplicates:
                continue
            sub_indices = []
            list_remainder = self.data[idx + 1 : ]
            for idx_inner, dict_obj_inner in enumerate(list_remainder):
                overall_idx = idx + idx_inner + 1
                if self._is_equal(dict_obj, dict_obj_inner, subset=subset):
                    indices_involved_in_duplicates.add(idx)
                    indices_involved_in_duplicates.add(overall_idx)
                    if not sub_indices:
                        sub_indices.append(idx)
                    sub_indices.append(overall_idx)
                    if break_at == "first":
                        return [sub_indices]
            if sub_indices:
                indices.append(sub_indices)
                if break_at == "first_full":
                    return indices
        return indices

    def _is_equal(
            self,
            d1: Dict[str, Any],
            d2: Dict[str, Any],
            /,
            *,
            subset: Optional[List[str]] = None,
        ) -> bool:
        """Compares the given 2 dictionaries based on the subset of keys"""
        if not subset:
            return d1 == d2
        for key in subset:
            try:
                are_equal: bool = d1[key] == d2[key]
            except KeyError:
                raise KeyError(f"Key '{key}' from subset is not found")
            if not are_equal:
                return False
        return True

    def has_duplicates(
            self,
            *,
            subset: Optional[List[str]] = None,
        ) -> bool:
        """Checks if the dataset has duplicate rows over the given `subset` of fields"""
        return bool(
            self._identify_duplicate_indices(break_at="first", subset=subset)
        )

    def drop_duplicates(
            self,
            *,
            keep: Optional[Literal["first", "last"]] = "first",
            subset: Optional[List[str]] = None,
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Drops the duplicate rows"""
        list_obj = self.data if inplace else self.data_copy()
        indices = self._identify_duplicate_indices(subset=subset)
        if not indices:
            return self if inplace else Dataset(list_obj)
        indices_to_drop = []
        for sub_indices in indices:
            if keep == "first":
                temp = list(set(sub_indices).difference(set([min(sub_indices)])))
                indices_to_drop.extend(temp)
            elif keep == "last":
                temp = list(set(sub_indices).difference(set([max(sub_indices)])))
                indices_to_drop.extend(temp)
        for idx in sorted(indices_to_drop, reverse=True):
            list_obj.pop(idx)
        return self if inplace else Dataset(list_obj)

    def get_values_by_field(self, *, field: str) -> List[Any]:
        """Returns a list of values for the given field"""
        values = []
        for idx, dict_obj in enumerate(self.data):
            try:
                value = dict_obj[field]
            except KeyError:
                raise KeyError(f"Field '{field}' is not found on row number {idx + 1}")
            values.append(value)
        return values

    def get_datatypes_by_field(self) -> Dict[str, set[Type]]:
        """Returns dictionary having keys = fields, and values = set of all the unique types present in said field"""
        datatypes_by_field: Dict[str, set[Type]] = {}
        for dict_obj in self.data:
            for field, value in dict_obj.items():
                datatypes_by_field.setdefault(field, set())
                datatype = type(value)
                datatypes_by_field[field].add(datatype)
        return datatypes_by_field

    def get_unique_fields(self) -> List[str]:
        """Returns list of all the unique fields that are present (sorted in ascending order)"""
        unique_fields = set()
        for dict_obj in self.data:
            unique_fields = unique_fields.union(set(dict_obj.keys()))
        return list(sorted(list(unique_fields), reverse=False))

    def set_defaults_for_fields(
            self,
            *,
            fields: List[str],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """
        Checks if the given fields are present in each dictionary in the list.
        If not present, sets their default value to `None`.
        """
        assert checks.is_list_of_instances_of_type(fields, type_=str, allow_empty=False), (
            "Param `fields` must be a non-empty list of strings"
        )
        list_obj = self.data if inplace else self.data_copy()
        for dict_obj in list_obj:
            for field in fields:
                dict_obj.setdefault(field, None)
        return self if inplace else Dataset(list_obj)

    def compute_field(
            self,
            *,
            field: str,
            func: Callable[[Dict[str, Any]], Any],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """
        Applies the given function `func` to each dictionary in the list, and stores the result of `func` in the key `field` of each dictionary.
        The `func` takes in the dictionary (row) as a parameter.
        """
        list_obj = self.data if inplace else self.data_copy()
        for dict_obj in list_obj:
            computed_value = func(dict_obj)
            dict_obj[field] = computed_value
        return self if inplace else Dataset(list_obj)

    def keep_fields(
            self,
            *,
            fields: List[str],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Keeps the given fields (if they exist)"""
        assert checks.is_list_of_instances_of_type(fields, type_=str, allow_empty=False), (
            "Param `fields` must be a non-empty list of strings"
        )
        fields_to_keep = set(fields)
        existing_fields = self.get_unique_fields()
        fields_to_drop = list(set(existing_fields).difference(fields_to_keep))
        if not fields_to_drop:
            return self if inplace else self.copy()
        instance = self.drop_fields(fields=fields_to_drop, inplace=inplace)
        return instance

    def drop_fields(
            self,
            *,
            fields: List[str],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Drops the given fields (if they exist)"""
        assert checks.is_list_of_instances_of_type(fields, type_=str, allow_empty=False), (
            "Param `fields` must be a non-empty list of strings"
        )
        list_obj = self.data if inplace else self.data_copy()
        for dict_obj in list_obj:
            for field in fields:
                dict_obj.pop(field, None)
        return self if inplace else Dataset(list_obj)

    def _has_all_unique_existing_fields_in_any_order(self, *, reordered_fields: List[str]) -> bool:
        existing_fields = self.get_unique_fields()
        return sorted(reordered_fields, reverse=False) == sorted(existing_fields, reverse=False)

    def reorder_fields(
            self,
            *,
            reordered_fields: List[str],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Re-orders the fields"""
        assert self._has_all_unique_existing_fields_in_any_order(reordered_fields=reordered_fields), (
            "Param `reordered_fields` must include all the unique existing fields (in any order)"
        )
        list_obj = self.data if inplace else self.data_copy()
        list_obj_new = []
        for idx, dict_obj in enumerate(list_obj):
            dict_obj_new = {}
            for field in reordered_fields:
                try:
                    value = dict_obj[field]
                except KeyError:
                    raise KeyError(f"Field '{field}' is not found on row number {idx + 1}")
                dict_obj_new[field] = value
            list_obj_new.append(dict_obj_new)

        if inplace:
            self.data = list_obj_new
        else:
            list_obj = list_obj_new

        return self if inplace else Dataset(list_obj)

    def fill_nulls(
            self,
            *,
            value: Any,
            subset: Optional[List[str]] = None,
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Fills all values that are `None` with `value`"""
        list_obj = self.data if inplace else self.data_copy()
        for dict_obj in list_obj:
            keys = subset if subset else list(dict_obj.keys())
            for key in keys:
                try:
                    existing_value = dict_obj[key]
                except KeyError:
                    raise KeyError(f"Key '{key}' from subset is not found")
                if existing_value is None:
                    dict_obj[key] = value
        return self if inplace else Dataset(list_obj)

    def autofill_missing_fields(
            self,
            *,
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """
        Checks if the existing unique fields are present in each dictionary in the list.
        If not present, sets their default value to `None`.
        """
        fields = self.get_unique_fields()
        instance = self.set_defaults_for_fields(fields=fields, inplace=inplace)
        return instance

    def _has_nulls(
            self,
            *,
            dict_obj: Dict[str, Any],
            subset: Optional[List[str]] = None,
        ) -> bool:
        """Checks if the given dictionary has value as `None` for any of the given `subset` of keys"""
        keys = subset if subset else list(dict_obj.keys())
        for key in keys:
            try:
                value = dict_obj[key]
            except KeyError:
                raise KeyError(f"Key '{key}' from subset is not found")
            if value is None:
                return True
        return False

    def drop_nulls(
            self,
            *,
            subset: Optional[List[str]] = None,
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Drops rows having value as `None` in any of the given `subset` of fields"""
        instance = self.filter_rows(
            func=lambda dict_obj: not self._has_nulls(dict_obj=dict_obj, subset=subset),
            inplace=inplace,
        )
        return instance

    def filter_rows(
            self,
            *,
            func: Callable[[Dict[str, Any]], bool],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """
        Applies the given function `func` to each dictionary (row) in the list, and expects the `func` to return a boolean.
        If the result is `True` then keeps the row; otherwise removes the row.
        The `func` takes in the dictionary (row) as a parameter.
        """
        list_obj = self.data if inplace else self.data_copy()
        list_obj_filtered: List[Dict[str, Any]] = []
        for dict_obj in list_obj:
            should_keep_row: bool = func(dict_obj)
            assert isinstance(should_keep_row, bool), f"Result of `func` must be of type boolean"
            if should_keep_row:
                list_obj_filtered.append(dict_obj)

        if inplace:
            self.data = list_obj_filtered
        else:
            list_obj = list_obj_filtered

        return self if inplace else Dataset(list_obj)

    def order_by(
            self,
            *,
            fields: List[str],
            ascending: List[bool],
        ) -> Dataset:
        """Orders by the given fields in the desired order. Returns a new instance having the ordered data."""
        assert checks.is_list_of_instances_of_type(fields, type_=str, allow_empty=False), (
            "Param `fields` must be a non-empty list of strings"
        )
        assert checks.is_list_of_instances_of_type(ascending, type_=bool, allow_empty=False), (
            "Param `ascending` must be a non-empty list of booleans"
        )
        assert len(fields) == len(ascending), "Params `fields` and `ascending` must be of same length"
        list_obj: List[Dict[str, Any]] = multi_key_sort(
            self.data,
            columns=fields,
            ascending=ascending,
        )
        return Dataset(list_obj)

    def concatenate(
            self,
            *,
            datasets: List[Dataset],
            inplace: Optional[bool] = False,
        ) -> Dataset:
        """Concatenates the current dataset with the given datasets. The given `datasets` are never modified."""
        assert checks.is_list_of_instances_of_type(datasets, type_=Dataset, allow_empty=True), (
            "Param `datasets` must be a list of datasets, each being of type `slupy.data_wrangler.dataset.Dataset`"
        )
        if not datasets:
            return self if inplace else self.copy()

        list_obj = self.data if inplace else self.data_copy()
        for dataset in datasets:
            list_obj += dataset.data_copy()

        if inplace:
            self.data = list_obj

        return self if inplace else Dataset(list_obj)

    def value_counts(self) -> Dict[str, Counter]:
        """
        Returns dictionary having keys = fields, and values = `collections.Counter` objects having the value-counts
        of all the values in said field.
        """
        result: Dict[str, Counter] = {}
        dataset_copy = self.copy()
        dataset_copy.autofill_missing_fields(inplace=True)
        existing_fields = dataset_copy.get_unique_fields()
        for field in existing_fields:
            values = dataset_copy.get_values_by_field(field=field)
            counter = Counter(values)
            result[field] = counter
        return result

    def pretty_print(self) -> None:
        """Pretty prints the value of `self.data`"""
        pprint(
            self.data,
            sort_dicts=False,
            underscore_numbers=False,
        )

