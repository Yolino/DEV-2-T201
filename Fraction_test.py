import unittest
from Fraction import Fraction

class MyTestCase(unittest.TestCase):

    def test_construct(self):
        f1 = Fraction(56, 98)
        result = f1
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 7)

        f2 = Fraction(0, 5)
        self.assertEqual(f2.numerator, 0)
        self.assertEqual(f2.denominator, 1)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

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

    def test_as_mixed_number(self):
        f1 = Fraction(7, 3)
        self.assertEqual(f1.as_mixed_number(), "2 1/3")
        f2 = Fraction(3, 1)
        self.assertEqual(f2.as_mixed_number(), "3")
        f3 = Fraction(1, 3)
        self.assertEqual(f3.as_mixed_number(), "1/3")
        f4 = Fraction(-7, 3)
        self.assertEqual(f4.as_mixed_number(), "-3 2/3")

    def test_add(self):
        f1 = Fraction(9, 3)
        f2 = Fraction(-1, 3)
        result = f1.__add__(f2)
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 3)
        f3 = Fraction(1, 5)
        f4 = Fraction(1, 6)
        result2 = f3.__add__(f4)
        self.assertEqual(result2.numerator, 11)
        self.assertEqual(result2.denominator, 30)

    def test_truediv(self):
        f1 = Fraction(9, 3)
        f2 = Fraction(1, 3)
        result = f1.__truediv__(f2)
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 1)

        f3 = Fraction(1, 2)
        f4 = Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            f3 / f4

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
        self.assertEqual(result, False)
        f2 = Fraction(2, 1)
        result2 = f2.is_proper()
        self.assertEqual(result2, True)

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
