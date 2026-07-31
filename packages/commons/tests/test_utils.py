import unittest
# Import the functions you want to test
from commons.utils import add, divide


class TestUtils(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Checks if add(2, 3) equals 5
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        # Checks if add(-1, -1) equals -2
        self.assertEqual(add(-1, -1), -2)

    def test_divide_normal(self):
        # Checks if divide(10, 2) equals 5.0
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        # Verifies that a ValueError is raised when dividing by zero
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()

