import unittest
from calculator import add, subtraction


class TestAdditionFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(100, 200), 300)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-100, -200), -300)

    def test_mixed_sign_numbers(self):
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(100, -200), -100)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 100), 100)
        self.assertEqual(add(-100, 0), -100)

    def test_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.1, -2.2), -3.3)
        self.assertAlmostEqual(add(100.123, 200.456), 300.579)

if __name__ == '__main__':
    unittest.main()
