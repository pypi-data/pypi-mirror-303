import unittest

from slupy.core import helpers


class Person:
    pass


class TestCore(unittest.TestCase):

    def test_create_repr(self):
        repr_string = helpers.create_repr(
            instance=Person(),
            kwargs_dict={"name": "james", "age": 42, "is_partner": False},
            multi_line=False,
        )
        self.assertEqual(
            repr_string,
            "Person(name='james', age=42, is_partner=False)",
        )

    def test_slice_by_position(self):
        sliceable_list = list(range(1, 30+1))
        sliceable_tuple = tuple(sliceable_list)
        sliceable_string = "hello world"

        self.assertEqual(
            helpers.slice_by_position(sliceable_list),
            sliceable_list,
        )
        self.assertEqual(
            helpers.slice_by_position(sliceable_list, start=5, end=12),
            list(range(5, 12+1)),
        )
        self.assertEqual(
            helpers.slice_by_position(sliceable_tuple, start=5, end=12),
            tuple(range(5, 12+1)),
        )
        self.assertEqual(
            helpers.slice_by_position(sliceable_string, start=2, end=8),
            "ello wo",
        )

    def test_compute_partitions(self):
        self.assertEqual(
            helpers.compute_partitions(length=100, zero_based=True, num_partitions=6),
            [(0, 16), (17, 33), (34, 50), (51, 67), (68, 84), (85, 99)],
        )
        self.assertEqual(
            helpers.compute_partitions(length=100, zero_based=False, num_partitions=6),
            [(1, 17), (18, 34), (35, 51), (52, 68), (69, 85), (86, 100)],
        )
        self.assertEqual(
            helpers.compute_partitions(length=100, zero_based=True, partition_size=17),
            [(0, 16), (17, 33), (34, 50), (51, 67), (68, 84), (85, 99)],
        )
        self.assertEqual(
            helpers.compute_partitions(length=100, zero_based=False, partition_size=17),
            [(1, 17), (18, 34), (35, 51), (52, 68), (69, 85), (86, 100)],
        )
        with self.assertRaises(AssertionError):
            helpers.compute_partitions(length=100, num_partitions=6, partition_size=17)
        with self.assertRaises(AssertionError):
            helpers.compute_partitions(length=0, num_partitions=6)
        with self.assertRaises(AssertionError):
            helpers.compute_partitions(length=0, partition_size=17)

    def test_rename_dict_keys(self):
        dictionary = {
            "aaa": 1,
            "bbb": 2,
            "ccc": {
                "c-k1": "v1",
                "c-k2": "v2",
                "c-k3": {
                    "c-kk1": "v1",
                    "c-kk2": "v2",
                    "c-kk3": "v3",
                },
            },
            "ddd": [
                {
                    "d-k1": 100,
                    "d-k2": 200,
                    "d-k3": 300,
                },
                {
                    "d-k1": 100,
                    "d-k2": 200,
                    "d-k3": 300,
                },
            ],
            "eee": (
                {
                    "e-k1": 100,
                    "e-k2": 200,
                    "e-k3": 300,
                },
                {
                    "e-k1": 100,
                    "e-k2": 200,
                    "e-k3": 300,
                },
            ),
            "FFF": "hello",
        }
        original_dictionary_id = id(dictionary)
        self.assertNotEqual(
            id(helpers.rename_dict_keys(dictionary, update_func=str.upper, deep=False)),
            original_dictionary_id,
        )
        self.assertNotEqual(
            id(helpers.rename_dict_keys(dictionary, update_func=str.upper, deep=True)),
            original_dictionary_id,
        )
        self.assertEqual(
            helpers.rename_dict_keys(dictionary, update_func=str.upper, deep=False),
            {
                "AAA": 1,
                "BBB": 2,
                "CCC": {
                    "c-k1": "v1",
                    "c-k2": "v2",
                    "c-k3": {
                        "c-kk1": "v1",
                        "c-kk2": "v2",
                        "c-kk3": "v3",
                    },
                },
                "DDD": [
                    {
                        "d-k1": 100,
                        "d-k2": 200,
                        "d-k3": 300,
                    },
                    {
                        "d-k1": 100,
                        "d-k2": 200,
                        "d-k3": 300,
                    },
                ],
                "EEE": (
                    {
                        "e-k1": 100,
                        "e-k2": 200,
                        "e-k3": 300,
                    },
                    {
                        "e-k1": 100,
                        "e-k2": 200,
                        "e-k3": 300,
                    },
                ),
                "FFF": "hello",
            },
        )
        self.assertEqual(
            helpers.rename_dict_keys(dictionary, update_func=str.upper, deep=True),
            {
                "AAA": 1,
                "BBB": 2,
                "CCC": {
                    "C-K1": "v1",
                    "C-K2": "v2",
                    "C-K3": {
                        "C-KK1": "v1",
                        "C-KK2": "v2",
                        "C-KK3": "v3",
                    },
                },
                "DDD": [
                    {
                        "D-K1": 100,
                        "D-K2": 200,
                        "D-K3": 300,
                    },
                    {
                        "D-K1": 100,
                        "D-K2": 200,
                        "D-K3": 300,
                    },
                ],
                "EEE": (
                    {
                        "E-K1": 100,
                        "E-K2": 200,
                        "E-K3": 300,
                    },
                    {
                        "E-K1": 100,
                        "E-K2": 200,
                        "E-K3": 300,
                    },
                ),
                "FFF": "hello",
            },
        )


