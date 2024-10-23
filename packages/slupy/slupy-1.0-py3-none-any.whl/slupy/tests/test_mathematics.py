import unittest

from slupy.mathematics import mathematics


class TestMathematics(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(mathematics.is_prime(2))
        self.assertTrue(mathematics.is_prime(3))
        self.assertTrue(not mathematics.is_prime(4))
        self.assertTrue(mathematics.is_prime(5))

    def test_cumulative_aggregate(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(
            mathematics.cumulative_aggregate(numbers=numbers, method="sum"),
            [1, 3, 6, 10, 15],
        )
        self.assertEqual(
            mathematics.cumulative_aggregate(numbers=numbers, method="difference"),
            [1, -1, -4, -8, -13],
        )
        self.assertEqual(
            mathematics.cumulative_aggregate(numbers=numbers, method="product"),
            [1, 2, 6, 24, 120],
        )
        self.assertEqual(
            mathematics.cumulative_aggregate(numbers=[1, 2 ,3], method="division"),
            [1, 1/2, 0.5/3],
        )

