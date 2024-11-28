class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRÉ : Prend un numérateur et un dénominateur en paramètre ce dernier ne peut pas être égal à 0
        POST : La fraction est stockée sous forme réduite avec un dénominateur positif
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        """GCD plus grand diviseur commun basé sur l'algorithme d'Euclide"""
        num_gcd = num
        den_gcd = den
        while den_gcd != 0:
            cache = num_gcd % den_gcd
            num_gcd = den_gcd
            den_gcd = cache
        common_divisor = num_gcd
        self._num = num // common_divisor
        self._den = abs(den // common_divisor)

    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRÉ : un object fraction
        POST : Retourne une chaîne de caractères représentant la fraction sous forme réduite
        """
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction.

        PRÉ : un object fraction
        POST : Retourne une chaîne de caractères représentant le résultat de la fraction avec son reste
        """
        integer_part = self.numerator // self.denominator
        remainder = abs(self.numerator % self.denominator)

        if remainder == 0:
            return str(integer_part)
        elif integer_part == 0:
            return f"{remainder}/{self.denominator}"
        else:
            return f"{integer_part} {remainder}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRÉ : Deux objets Fraction
        POST : Retourne une nouvelle fraction représentant la somme des deux fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRÉ : Deux objets Fraction
        POST : Retourne une nouvelle fraction représentant la différence des deux fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRÉ : Deux objets Fraction
        POST : Retourne une nouvelle fraction représentant le produit des deux fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRÉ : Deux objets Fraction
        POST : Retourne une nouvelle fraction représentant le quotient des deux fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be fractions.")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions

        PRÉ : UN objet Fraction ainsi qu'un entier
        POST : Retourne une nouvelle fraction représentant la puissance
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")
        num = self.numerator ** power
        den = self.denominator ** power
        return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRÉ : Deux objets Fraction
        POST : Retourne True si les deux fractions sont égales, sinon False
        """
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRÉ : Un objet Fraction
        POST : Retourne un float représentant la fraction
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRÉ : Un objet Fraction
        POST : Retourne True si la fraction vaut 0, sinon False
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRÉ : Un objet Fraction
        POST : Retourne True si la fraction est un entier, sinon False
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRÉ : Un objet Fraction
        POST : Retourne True si la fraction supérieur à 1, sinon False
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRÉ : Un objet Fraction
        POST : Retourne True si le numérateur vaut 1, sinon False
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        PRÉ : Deux objets Fraction
        POST : Retourne True si les deux fractions sont différentes d'une fraction unitaire, sinon False
        """
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        difference = Fraction(abs(num), den)
        return difference.numerator == 1 and difference.denominator != 0

def test():

    f1 = Fraction(4, 2)
    f2 = Fraction(1, 3)
    print(f1)
    print(f2.as_mixed_number())
    print(f1.__add__(f2))
    print(f1.__sub__(f2))
    print(f1.__mul__(f2))
    print(f1.__truediv__(f2))
    print(f1.__pow__(2))
    print(f1.__eq__(f2))
    print(f1.__float__())
    print(f1.is_zero())
    print(f1.is_integer())
    print(f1.is_proper())
    print(f1.is_unit())
    print(f1.is_adjacent_to(f2))

#test()