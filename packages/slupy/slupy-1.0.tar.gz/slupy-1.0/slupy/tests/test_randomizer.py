import unittest

from slupy.randomizer import randomizer


class TestRandomizer(unittest.TestCase):

    def test_generate_random_string(self):
        self.assertTrue(
            len(randomizer.generate_random_string(length=10)) == 10,
        )
        with self.assertRaises(AssertionError):
            randomizer.generate_random_string(
                length=10,
                include_lowercase=False,
                include_uppercase=False,
                include_digits=False,
                include_punctuations=False,
            )

    def test_generate_random_hex_code(self):
        random_hex_code = randomizer.generate_random_hex_code()
        self.assertTrue(
            len(random_hex_code) == 7
            and random_hex_code.startswith("#")
            and " " not in random_hex_code
        )

