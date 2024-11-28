import unittest
from Fraction import Fraction

class MyTestCase(unittest.TestCase):

    def test_construct(self):
        f1 = Fraction(56, 98)
        result = f1
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 7)

    def test_str(self):
        f1 = Fraction(1, 2)
        self.assertEqual(str(f1), "1/2")
        f2 = Fraction(-1, 2)
        self.assertEqual(str(f2), "-1/2")
        f3 = Fraction(1, -3)
        self.assertEqual(str(f3), "-1/3")
        f4 = Fraction(3, -3)
        self.assertEqual(str(f4), "-1")
        f5 = Fraction(0, 3)
        self.assertEqual(str(f5), "0")
        f6 = Fraction(-1, -3)
        self.assertEqual(str(f6), "1/3")

    def test_add(self):
        f1 = Fraction(9, 3)
        f2 = Fraction(-1, 3)
        result = f1.__add__(f2)
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 3)

    def test_truediv(self):
        f1 = Fraction(9, 3)
        f2 = Fraction(1,3)
        result = f1.__truediv__(f2)
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 1)

    def test_eq(self):
        f1 = Fraction(8, 16)
        f2 = Fraction(1, 2)
        result = f1.__eq__(f2)
        self.assertEqual(result, True)
        f3 = Fraction(1, 16)
        f4 = Fraction(2, 16)
        result2 = f3.__eq__(f4)
        self.assertEqual(result2, False)

    def test_integer(self):
        f1 = Fraction(8, 8)
        result = f1.is_integer()
        self.assertEqual(result, True)
        f2 = Fraction(1, 2)
        result2 = f2.is_integer()
        self.assertEqual(result2, False)

    def test_proper(self):
        f1 = Fraction(1, 2)
        result = f1.is_proper()
        self.assertEqual(result, True)
        f2 = Fraction(2, 1)
        result2 = f2.is_proper()
        self.assertEqual(result2, False)

    def test_adjacent_to(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(1, 3)
        result = f1.is_adjacent_to(f2)
        self.assertEqual(result, True)
        f3 = Fraction(2, 3)
        f4 = Fraction(1, 4)
        result2 = f3.is_adjacent_to(f4)
        self.assertEqual(result2, False)


if __name__ == '__main__':
    unittest.main()
