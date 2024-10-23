import unittest

from slupy.strings import strings


class TestStrings(unittest.TestCase):

    def test_string_case_conversions(self):
        self.assertEqual(
            strings.camel_to_pascal("helloAndGoodMorning"),
            "HelloAndGoodMorning",
        )
        self.assertEqual(
            strings.camel_to_snake("helloAndGoodMorning"),
            "hello_and_good_morning",
        )
        self.assertEqual(
            strings.pascal_to_camel("HelloAndGoodMorning"),
            "helloAndGoodMorning",
        )
        self.assertEqual(
            strings.pascal_to_snake("HelloAndGoodMorning"),
            "hello_and_good_morning",
        )
        self.assertEqual(
            strings.snake_to_pascal("hello_and_good_morning"),
            "HelloAndGoodMorning",
        )
        self.assertEqual(
            strings.snake_to_camel("hello_and_good_morning"),
            "helloAndGoodMorning",
        )
        self.assertEqual(
            strings.snake_to_kebab("hello_and_good_morning"),
            "hello-and-good-morning",
        )
        self.assertEqual(
            strings.kebab_to_snake("hello-and-good-morning"),
            "hello_and_good_morning",
        )

    def test_string_slicing(self):
        self.assertEqual(
            strings.get_first_n_characters(text="hello-world", num_chars=4),
            "hell",
        )
        self.assertEqual(
            strings.get_last_n_characters(text="hello-world", num_chars=4),
            "orld",
        )
        self.assertEqual(
            strings.remove_first_n_characters(text="hello-world", num_chars=4),
            "o-world",
        )
        self.assertEqual(
            strings.remove_last_n_characters(text="hello-world", num_chars=4),
            "hello-w",
        )

    def test_remove_characters_at_indices(self):
        self.assertEqual(
            strings.remove_characters_at_indices(text="hello and good morning", indices=[]),
            "hello and good morning",
        )
        self.assertEqual(
            strings.remove_characters_at_indices(text="hello and good morning", indices=[6, 8, 11, 21]),
            "hello n god mornin",
        )
        with self.assertRaises(IndexError):
            strings.remove_characters_at_indices(text="hello and good morning", indices=[-1])
        with self.assertRaises(IndexError):
            strings.remove_characters_at_indices(text="hello and good morning", indices=[22])
        with self.assertRaises(IndexError):
            strings.remove_characters_at_indices(text="hello and good morning", indices=[100])

    def test_remove_characters_at_positions(self):
        self.assertEqual(
            strings.remove_characters_at_positions(text="hello and good morning", positions=[]),
            "hello and good morning",
        )
        self.assertEqual(
            strings.remove_characters_at_positions(text="hello and good morning", positions=[7, 9, 12, 22]),
            "hello n god mornin",
        )
        with self.assertRaises(IndexError):
            strings.remove_characters_at_positions(text="hello and good morning", positions=[0])
        with self.assertRaises(IndexError):
            strings.remove_characters_at_positions(text="hello and good morning", positions=[23])
        with self.assertRaises(IndexError):
            strings.remove_characters_at_positions(text="hello and good morning", positions=[101])

    def test_to_dumbo_text(self):
        self.assertEqual(
            strings.to_dumbo_text("Hello, and good morning!"),
            "hElLo, AnD gOoD mOrNiNg!",
        )

    def test_make_message(self):
        self.assertEqual(
            strings.make_message("hello", prefix="prefix", suffix="suffix", sep="|"),
            "prefix|hello|suffix",
        )

    def test_is_part_of_charset(self):
        charset = set(list("aeiouAEIOU._-"))
        self.assertTrue(
            strings.is_part_of_charset(text="auoiAEEE...__.._--AAUUUiii", charset=charset),
        )
        self.assertTrue(
            not strings.is_part_of_charset(text="aer", charset=charset),
        )

    def test_is_snake_case(self):
        self.assertTrue(
            strings.is_snake_case("hello123"),
        )
        self.assertTrue(
            strings.is_snake_case("hello1_world1"),
        )
        self.assertTrue(
            not strings.is_snake_case("123_hello1_world1"),
        )
        self.assertTrue(
            not strings.is_snake_case("hello-world"),
        )
        self.assertTrue(
            not strings.is_snake_case("Hello_world"),
        )
        self.assertTrue(
            not strings.is_snake_case("h.ello_world"),
        )
        self.assertTrue(
            not strings.is_snake_case("hello_world_"),
        )
        self.assertTrue(
            strings.is_snake_case("HELLO_WORLD_123_YES", as_uppercase=True),
        )
        self.assertTrue(
            not strings.is_snake_case("hello_world", as_uppercase=True),
        )
        self.assertTrue(
            strings.is_snake_case("HELLO123", as_uppercase=True),
        )
        self.assertTrue(
            not strings.is_snake_case(""),
        )

    def test_is_kebab_case(self):
        self.assertTrue(
            strings.is_kebab_case("hello123"),
        )
        self.assertTrue(
            strings.is_kebab_case("hello1-world1-123-yes-000"),
        )
        self.assertTrue(
            not strings.is_kebab_case("123-hello1-world1-123-yes-000"),
        )
        self.assertTrue(
            not strings.is_kebab_case("hello_world"),
        )
        self.assertTrue(
            not strings.is_kebab_case("Hello-world"),
        )
        self.assertTrue(
            not strings.is_kebab_case("h.ello-world"),
        )
        self.assertTrue(
            not strings.is_kebab_case("hello-world-"),
        )
        self.assertTrue(
            strings.is_kebab_case("HELLO-WORLD123-YES-000", as_uppercase=True),
        )
        self.assertTrue(
            not strings.is_kebab_case("hello-world", as_uppercase=True),
        )
        self.assertTrue(
            strings.is_kebab_case("HELLO", as_uppercase=True),
        )
        self.assertTrue(
            not strings.is_kebab_case(""),
        )

    def test_is_camel_case(self):
        self.assertTrue(
            strings.is_camel_case("hello"),
        )
        self.assertTrue(
            strings.is_camel_case("helloWorld"),
        )
        self.assertTrue(
            not strings.is_camel_case("0helloWorld"),
        )
        self.assertTrue(
            not strings.is_camel_case("hello-world"),
        )
        self.assertTrue(
            not strings.is_camel_case("hello_world"),
        )
        self.assertTrue(
            strings.is_camel_case("hELLOWORLD"),
        )
        self.assertTrue(
            not strings.is_camel_case("HELLOWORLD"),
        )
        self.assertTrue(
            not strings.is_camel_case(""),
        )

    def test_is_pascal_case(self):
        self.assertTrue(
            strings.is_pascal_case("Hello"),
        )
        self.assertTrue(
            strings.is_pascal_case("HelloWorld"),
        )
        self.assertTrue(
            not strings.is_pascal_case("0HelloWorld"),
        )
        self.assertTrue(
            not strings.is_pascal_case("Hello-world"),
        )
        self.assertTrue(
            not strings.is_pascal_case("Hello_world"),
        )
        self.assertTrue(
            strings.is_pascal_case("HELLOWORLD"),
        )
        self.assertTrue(
            not strings.is_pascal_case(""),
        )

