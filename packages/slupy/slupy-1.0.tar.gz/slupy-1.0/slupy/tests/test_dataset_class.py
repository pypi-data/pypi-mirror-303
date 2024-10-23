from datetime import datetime
from typing import Any, Dict, List
import unittest
import uuid

from slupy.core.helpers import make_deep_copy
from slupy.data_wrangler.dataset import Dataset


class TestDataset(unittest.TestCase):

    def setUp(self) -> None:
        self.list_data_1 = [
            {
                "index": 1,
                "text": "AAA",
                "number": 10,
            },
            {
                "index": 2,
                "text": "AAA",
                "number": 20,
            },
            {
                "index": 3,
                "text": "AAA",
                "number": 30,
            },
            {
                "index": 4,
                "text": "BBB",
                "number": -1,
            },
            {
                "index": 5,
                "text": "BBB",
                "number": -1,
            },
            {
                "index": 6,
                "text": "BBB",
                "number": -5,
            },
            {
                "index": 7,
                "text": "CCC",
                "number": 45,
            },
            {
                "index": 8,
                "text": "CCC",
                "number": 50,
            },
            {
                "index": 9,
                "text": "CCC",
                "number": 50,
            },
        ]
        self.list_data_1_copy = make_deep_copy(self.list_data_1)
        self.list_data_2 = [
            {
                "index": 1,
                "text": "AAA",
                "number": 10,
            },
            {
                "index": 4,
                "text": "BBB",
                "number": -1,
            },
            {
                "index": 7,
                "text": "CCC",
                "number": 45,
            },
        ]
        self.list_data_2_copy = make_deep_copy(self.list_data_2)
        self.list_data_3 = [
            {
                "index": 1,
                "text": None,
            },
            {
                "index": 2,
                "text": "BBB",
            },
            {
                "index": None,
                "text": None,
            },
            {
                "index": 4,
                "text": "DDD",
            },
        ]
        self.list_data_3_copy = make_deep_copy(self.list_data_3)
        self.list_data_4 = [
            {
                "a": 1,
                "b": 2,
                "c": 3,
            },
            {
                "a": 10,
                "b": 20,
            },
            {
                "a": 100,
                "b": 200,
            },
        ]
        self.list_data_4_copy = make_deep_copy(self.list_data_4)
        self.list_data_5 = [
            {
                "text": None,
                "number": 50,
            },
            {
                "text": "BBB",
                "number": None,
            },
            {
                "text": "AAA",
                "number": -1,
            },
            {
                "text": "BBB",
                "number": -1,
            },
            {
                "text": None,
                "number": None,
            },
            {
                "text": "AAA",
                "number": 50,
            },
            {
                "text": "BBB",
                "number": 50,
            },
            {
                "text": "BBB",
                "number": 20,
            },
            {
                "text": "AAA",
                "number": 5,
            },
        ]
        self.list_data_5_copy = make_deep_copy(self.list_data_5)
        self.list_data_6 = [
            {
                "a": "aaa",
                "b": 123,
                "c": uuid.uuid4(),
            },
            {
                "a": b"aaa",
                "b": 1.23,
                "c": datetime.now(),
            },
            {
                "a": uuid.uuid4(),
                "b": None,
                "c": 1.23,
            },
            {
                "a": datetime.now(),
                "b": "bbb",
                "c": None,
            },
        ]
        self.list_data_6_copy = make_deep_copy(self.list_data_6)

    def _assert_list_data_is_unchanged(self):
        msg = "The value of list data should not be modified in-place"

        self.assertEqual(
            self.list_data_1,
            self.list_data_1_copy,
            msg=msg,
        )
        self.assertNotEqual(
            id(self.list_data_1),
            id(self.list_data_1_copy),
        )

        self.assertEqual(
            self.list_data_2,
            self.list_data_2_copy,
            msg=msg,
        )
        self.assertNotEqual(
            id(self.list_data_2),
            id(self.list_data_2_copy),
        )

        self.assertEqual(
            self.list_data_3,
            self.list_data_3_copy,
            msg=msg,
        )
        self.assertNotEqual(
            id(self.list_data_3),
            id(self.list_data_3_copy),
        )

        self.assertEqual(
            self.list_data_4,
            self.list_data_4_copy,
            msg=msg,
        )
        self.assertNotEqual(
            id(self.list_data_4),
            id(self.list_data_4_copy),
        )

        self.assertEqual(
            self.list_data_5,
            self.list_data_5_copy,
            msg=msg,
        )
        self.assertNotEqual(
            id(self.list_data_5),
            id(self.list_data_5_copy),
        )

        self.assertEqual(
            self.list_data_6,
            self.list_data_6_copy,
            msg=msg,
        )
        self.assertNotEqual(
            id(self.list_data_6),
            id(self.list_data_6_copy),
        )

    def test_len(self):
        dataset = Dataset(self.list_data_1)
        self.assertEqual(len(dataset), len(dataset.data))
        self._assert_list_data_is_unchanged()

    def test_getitem(self):
        dataset = Dataset(self.list_data_1)

        self.assertEqual(dataset[0], dataset.data[0])
        self.assertEqual(dataset[-1], dataset.data[-1])

        with self.assertRaises(IndexError):
            dataset[len(dataset)]  # Should always raise IndexError since len(dataset) will always be > it's last index

        self._assert_list_data_is_unchanged()

    def test_has_duplicates(self):
        dataset = Dataset(self.list_data_1)

        self.assertTrue(not dataset.has_duplicates())
        self.assertTrue(dataset.has_duplicates(subset=["text"]))
        self.assertTrue(dataset.has_duplicates(subset=["text", "number"]))

        with self.assertRaises(KeyError):
            dataset.has_duplicates(subset=["text", "number", "key-that-does-not-exist"])

        with self.assertRaises(KeyError):
            dataset.has_duplicates(subset=["key-that-does-not-exist"])

        self._assert_list_data_is_unchanged()

    def test_drop_duplicates(self):
        dataset = Dataset(self.list_data_1)

        result_1 = dataset.drop_duplicates(keep="first", subset=["text", "number"]).data
        self.assertEqual(len(result_1), 7)

        result_2 = dataset.drop_duplicates(keep="first", subset=["text"]).data
        self.assertEqual(len(result_2), 3)
        self.assertEqual(
            result_2,
            [
                {
                    "index": 1,
                    "text": "AAA",
                    "number": 10,
                },
                {
                    "index": 4,
                    "text": "BBB",
                    "number": -1,
                },
                {
                    "index": 7,
                    "text": "CCC",
                    "number": 45,
                },
            ],
        )

        result_3 = dataset.drop_duplicates(keep="last", subset=["text"]).data
        self.assertEqual(len(result_3), 3)
        self.assertEqual(
            result_3,
            [
                {
                    "index": 3,
                    "text": "AAA",
                    "number": 30,
                },
                {
                    "index": 6,
                    "text": "BBB",
                    "number": -5,
                },
                {
                    "index": 9,
                    "text": "CCC",
                    "number": 50,
                },
            ],
        )

        self._assert_list_data_is_unchanged()

    def test_drop_duplicates_inplace(self):
        dataset = Dataset(self.list_data_1, deep_copy=True)
        dataset.drop_duplicates(keep="last", subset=["text"], inplace=True)
        result = dataset.data
        self.assertEqual(len(result), 3)
        self.assertEqual(
            result,
            [
                {
                    "index": 3,
                    "text": "AAA",
                    "number": 30,
                },
                {
                    "index": 6,
                    "text": "BBB",
                    "number": -5,
                },
                {
                    "index": 9,
                    "text": "CCC",
                    "number": 50,
                },
            ],
        )
        self._assert_list_data_is_unchanged()

    def test_get_values_by_field(self):
        dataset = Dataset(self.list_data_4)

        self.assertEqual(
            dataset.get_values_by_field(field="a"),
            [1, 10, 100],
        )
        self.assertEqual(
            dataset.get_values_by_field(field="b"),
            [2, 20, 200],
        )

        with self.assertRaises(KeyError):
            dataset.get_values_by_field(field="c")

        self._assert_list_data_is_unchanged()

    def test_get_datatypes_by_field(self):
        dataset = Dataset(self.list_data_6)
        datatypes_by_field = dataset.get_datatypes_by_field()
        types_of_field_a = datatypes_by_field.get("a", set())
        types_of_field_b = datatypes_by_field.get("b", set())
        types_of_field_c = datatypes_by_field.get("c", set())
        self.assertIsInstance(types_of_field_a, set)
        self.assertIsInstance(types_of_field_b, set)
        self.assertIsInstance(types_of_field_c, set)
        self.assertEqual(len(types_of_field_a), 4)
        self.assertEqual(len(types_of_field_b), 4)
        self.assertEqual(len(types_of_field_c), 4)
        self.assertTrue(
            all([dtype in types_of_field_a for dtype in [uuid.UUID, bytes, str, datetime]])
        )
        self.assertTrue(
            all([dtype in types_of_field_b for dtype in [int, str, float, type(None)]])
        )
        self.assertTrue(
            all([dtype in types_of_field_c for dtype in [uuid.UUID, type(None), float, datetime]])
        )
        self._assert_list_data_is_unchanged()

    def test_get_unique_fields(self):
        dataset = Dataset(self.list_data_1, deep_copy=True)
        self.assertEqual(
            dataset.get_unique_fields(),
            ["index", "number", "text"],
        )
        self._assert_list_data_is_unchanged()

        dataset.compute_field(field="new_field", func=lambda d: None, inplace=True)
        self.assertEqual(
            dataset.get_unique_fields(),
            ["index", "new_field", "number", "text"],
        )
        self._assert_list_data_is_unchanged()

    def test_set_defaults_for_fields(self):
        dataset = Dataset(self.list_data_4)
        result = dataset.set_defaults_for_fields(fields=["c", "d"]).data
        result_expected = [
            {
                "a": 1,
                "b": 2,
                "c": 3,
                "d": None,
            },
            {
                "a": 10,
                "b": 20,
                "c": None,
                "d": None,
            },
            {
                "a": 100,
                "b": 200,
                "c": None,
                "d": None,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_set_defaults_for_fields_inplace(self):
        dataset = Dataset(self.list_data_4, deep_copy=True)
        dataset.set_defaults_for_fields(fields=["c", "d"], inplace=True)
        result = dataset.data
        result_expected = [
            {
                "a": 1,
                "b": 2,
                "c": 3,
                "d": None,
            },
            {
                "a": 10,
                "b": 20,
                "c": None,
                "d": None,
            },
            {
                "a": 100,
                "b": 200,
                "c": None,
                "d": None,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_compute_field(self):
        dataset = Dataset(self.list_data_1)
        result = dataset.compute_field(field="index", func=lambda d: d["index"] + 100).data

        result_expected = []
        for item in Dataset(self.list_data_1).data_copy():
            item["index"] += 100
            result_expected.append(item)

        self.assertEqual(result, result_expected)

        with self.assertRaises(KeyError):
            dataset.compute_field(field="index", func=lambda d: d["--index--"] + 100)

        self._assert_list_data_is_unchanged()

    def test_compute_field_inplace(self):
        dataset = Dataset(self.list_data_1, deep_copy=True)
        dataset.compute_field(field="index", func=lambda d: d["index"] + 100, inplace=True)
        result = dataset.data

        result_expected = []
        for item in Dataset(self.list_data_1).data_copy():
            item["index"] += 100
            result_expected.append(item)

        self.assertEqual(result, result_expected)

        with self.assertRaises(KeyError):
            dataset.compute_field(field="index", func=lambda d: d["--index--"] + 100, inplace=True)

        self._assert_list_data_is_unchanged()

    def test_keep_fields(self):
        dataset = Dataset(self.list_data_2)
        result = dataset.keep_fields(fields=["number", "text", "key-that-does-not-exist"]).data
        result_expected = [
            {
                "text": "AAA",
                "number": 10,
            },
            {
                "text": "BBB",
                "number": -1,
            },
            {
                "text": "CCC",
                "number": 45,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_keep_fields_inplace(self):
        dataset = Dataset(self.list_data_2, deep_copy=True)
        dataset.keep_fields(fields=["number", "text", "key-that-does-not-exist"], inplace=True)
        result = dataset.data
        result_expected = [
            {
                "text": "AAA",
                "number": 10,
            },
            {
                "text": "BBB",
                "number": -1,
            },
            {
                "text": "CCC",
                "number": 45,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_drop_fields(self):
        dataset = Dataset(self.list_data_2)
        result = dataset.drop_fields(fields=["number", "key-that-does-not-exist"]).data
        result_expected = [
            {
                "index": 1,
                "text": "AAA",
            },
            {
                "index": 4,
                "text": "BBB",
            
            },
            {
                "index": 7,
                "text": "CCC",
            
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_drop_fields_inplace(self):
        dataset = Dataset(self.list_data_2, deep_copy=True)
        dataset.drop_fields(fields=["number", "key-that-does-not-exist"], inplace=True)
        result = dataset.data
        result_expected = [
            {
                "index": 1,
                "text": "AAA",
            },
            {
                "index": 4,
                "text": "BBB",
            
            },
            {
                "index": 7,
                "text": "CCC",
            
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def _assert_order_of_fields(self, *, expected_order: List[str], list_data: List[Dict[str, Any]]):
        for idx, row in enumerate(list_data):
            self.assertEqual(
                expected_order,
                list(row.keys()),
                msg=f"Field order did not match at row number {idx + 1}",
            )

    def test_reorder_fields(self):
        dataset = Dataset(self.list_data_2)
        reordered_fields = ["text", "index", "number"]
        result = dataset.reorder_fields(reordered_fields=reordered_fields).data
        self._assert_order_of_fields(expected_order=reordered_fields, list_data=result)
        self._assert_list_data_is_unchanged()

    def test_reorder_fields_inplace(self):
        dataset = Dataset(self.list_data_2, deep_copy=True)
        reordered_fields = ["text", "index", "number"]
        dataset.reorder_fields(reordered_fields=reordered_fields, inplace=True)
        result = dataset.data
        self._assert_order_of_fields(expected_order=reordered_fields, list_data=result)
        self._assert_list_data_is_unchanged()

    def test_fill_nulls(self):
        dataset = Dataset(self.list_data_3)

        self.assertEqual(
            dataset.fill_nulls(value="<HELLO>").data,
            [
                {
                    "index": 1,
                    "text": "<HELLO>",
                },
                {
                    "index": 2,
                    "text": "BBB",
                },
                {
                    "index": "<HELLO>",
                    "text": "<HELLO>",
                },
                {
                    "index": 4,
                    "text": "DDD",
                },
            ],
        )
        self._assert_list_data_is_unchanged()

        self.assertEqual(
            dataset.fill_nulls(value="<HELLO>", subset=["text"]).data,
            [
                {
                    "index": 1,
                    "text": "<HELLO>",
                },
                {
                    "index": 2,
                    "text": "BBB",
                },
                {
                    "index": None,
                    "text": "<HELLO>",
                },
                {
                    "index": 4,
                    "text": "DDD",
                },
            ],
        )
        self._assert_list_data_is_unchanged()

    def test_fill_nulls_inplace(self):
        dataset_1 = Dataset(self.list_data_3, deep_copy=True)
        self.assertEqual(
            dataset_1.fill_nulls(value="<HELLO>", inplace=True).data,
            [
                {
                    "index": 1,
                    "text": "<HELLO>",
                },
                {
                    "index": 2,
                    "text": "BBB",
                },
                {
                    "index": "<HELLO>",
                    "text": "<HELLO>",
                },
                {
                    "index": 4,
                    "text": "DDD",
                },
            ],
        )
        self._assert_list_data_is_unchanged()

        dataset_2 = Dataset(self.list_data_3, deep_copy=True)
        self.assertEqual(
            dataset_2.fill_nulls(value="<HELLO>", subset=["text"], inplace=True).data,
            [
                {
                    "index": 1,
                    "text": "<HELLO>",
                },
                {
                    "index": 2,
                    "text": "BBB",
                },
                {
                    "index": None,
                    "text": "<HELLO>",
                },
                {
                    "index": 4,
                    "text": "DDD",
                },
            ],
        )
        self._assert_list_data_is_unchanged()

    def test_autofill_from_init(self):
        dataset = Dataset(self.list_data_4, deep_copy=True, autofill=True)
        result = dataset.data
        result_expected = [
            {
                "a": 1,
                "b": 2,
                "c": 3,
            },
            {
                "a": 10,
                "b": 20,
                "c": None,
            },
            {
                "a": 100,
                "b": 200,
                "c": None,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_autofill_missing_fields(self):
        dataset = Dataset(self.list_data_4)
        result = dataset.autofill_missing_fields().data
        result_expected = [
            {
                "a": 1,
                "b": 2,
                "c": 3,
            },
            {
                "a": 10,
                "b": 20,
                "c": None,
            },
            {
                "a": 100,
                "b": 200,
                "c": None,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_autofill_missing_fields_inplace(self):
        dataset = Dataset(self.list_data_4, deep_copy=True)
        dataset.autofill_missing_fields(inplace=True)
        result = dataset.data
        result_expected = [
            {
                "a": 1,
                "b": 2,
                "c": 3,
            },
            {
                "a": 10,
                "b": 20,
                "c": None,
            },
            {
                "a": 100,
                "b": 200,
                "c": None,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_drop_nulls(self):
        dataset = Dataset(self.list_data_3)

        result_1 = dataset.drop_nulls().data
        result_expected_1 = [
            {
                "index": 2,
                "text": "BBB",
            },
            {
                "index": 4,
                "text": "DDD",
            },
        ]
        self.assertEqual(result_1, result_expected_1)
        self._assert_list_data_is_unchanged()

        result_2 = dataset.drop_nulls(subset=["index"]).data
        result_expected_2 = [
            {
                "index": 1,
                "text": None,
            },
            {
                "index": 2,
                "text": "BBB",
            },
            {
                "index": 4,
                "text": "DDD",
            },
        ]
        self.assertEqual(result_2, result_expected_2)
        self._assert_list_data_is_unchanged()

    def test_drop_nulls_inplace(self):
        dataset_1 = Dataset(self.list_data_3, deep_copy=True)
        dataset_1.drop_nulls(inplace=True)
        result_1 = dataset_1.data
        result_expected_1 = [
            {
                "index": 2,
                "text": "BBB",
            },
            {
                "index": 4,
                "text": "DDD",
            },
        ]
        self.assertEqual(result_1, result_expected_1)
        self._assert_list_data_is_unchanged()

        dataset_2 = Dataset(self.list_data_3, deep_copy=True)
        dataset_2.drop_nulls(subset=["index"], inplace=True)
        result_2 = dataset_2.data
        result_expected_2 = [
            {
                "index": 1,
                "text": None,
            },
            {
                "index": 2,
                "text": "BBB",
            },
            {
                "index": 4,
                "text": "DDD",
            },
        ]
        self.assertEqual(result_2, result_expected_2)
        self._assert_list_data_is_unchanged()

    def test_filter_rows(self):
        dataset = Dataset(self.list_data_1)
        
        with self.assertRaises(AssertionError):
            dataset.filter_rows(func=lambda d: d)
        
        result = dataset.filter_rows(func=lambda d: d["text"] == "AAA" and d["index"] % 2 != 0).data
        result_expected = [
            {
                "index": 1,
                "text": "AAA",
                "number": 10,
            },
            {
                "index": 3,
                "text": "AAA",
                "number": 30,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_filter_rows_inplace(self):
        dataset = Dataset(self.list_data_1, deep_copy=True)
        
        with self.assertRaises(AssertionError):
            dataset.filter_rows(func=lambda d: d, inplace=True)

        dataset.filter_rows(func=lambda d: d["text"] == "AAA" and d["index"] % 2 != 0, inplace=True)
        result = dataset.data
        result_expected = [
            {
                "index": 1,
                "text": "AAA",
                "number": 10,
            },
            {
                "index": 3,
                "text": "AAA",
                "number": 30,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_order_by(self):
        dataset = Dataset(self.list_data_5)
        dataset_ordered = dataset.order_by(fields=["number", "text"], ascending=[False, False])
        self.assertNotEqual(
            id(dataset),
            id(dataset_ordered),
        )
        result = dataset_ordered.data
        result_expected = [
            {
                "text": "BBB",
                "number": 50,
            },
            {
                "text": "AAA",
                "number": 50,
            },
            {
                "text": None,
                "number": 50,
            },
            {
                "text": "BBB",
                "number": 20,
            },
            {
                "text": "AAA",
                "number": 5,
            },
            {
                "text": "BBB",
                "number": -1,
            },
            {
                "text": "AAA",
                "number": -1,
            },
            {
                "text": "BBB",
                "number": None,
            },
            {
                "text": None,
                "number": None,
            },
        ]
        self.assertEqual(result, result_expected)
        self._assert_list_data_is_unchanged()

    def test_concatenate(self):
        dataset = Dataset(self.list_data_4)
        initial_length = len(dataset)
        datasets_to_concatenate = [
            Dataset(self.list_data_1),
            Dataset(self.list_data_2),
            Dataset(self.list_data_3),
        ]
        expected_length = initial_length + sum(len(x) for x in datasets_to_concatenate)

        dataset_new = dataset.concatenate(datasets=datasets_to_concatenate)
        self.assertEqual(
            len(dataset_new),
            expected_length,
        )
        self._assert_list_data_is_unchanged()

    def test_concatenate_inplace(self):
        dataset = Dataset(self.list_data_4, deep_copy=True)
        initial_length = len(dataset)
        datasets_to_concatenate = [
            Dataset(self.list_data_1),
            Dataset(self.list_data_2),
            Dataset(self.list_data_3),
        ]
        expected_length = initial_length + sum(len(x) for x in datasets_to_concatenate)

        dataset.concatenate(datasets=datasets_to_concatenate, inplace=True)
        self.assertEqual(
            len(dataset),
            expected_length,
        )
        self._assert_list_data_is_unchanged()

