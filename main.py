class Fraction:

  def __init__(self, numerator, denominator):

    self.numerator = numerator
    self.denominator = denominator

  def __str__(self):

    return f"{self.numerator}/{self.denominator}"

  def __add__(self, other):

    new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)

  def __sub__(self, other):

    new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)

  def __mul__(self, other):

    new_numerator = self.numerator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)

  def __truediv__(self, other):

    new_numerator = self.numerator * other.denominator
    new_denominator = self.denominator * other.numerator
    return Fraction(new_numerator, new_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(f"Дріб 1: {fraction1}")
print(f"Дріб 2: {fraction2}")

sum_fraction = fraction1 + fraction2
difference_fraction = fraction1 - fraction2
product_fraction = fraction1 * fraction2
quotient_fraction = fraction1 / fraction2

print(f"Сума: {sum_fraction}")
print(f"Різниця: {difference_fraction}")
print(f"Добуток: {product_fraction}")
print(f"Частка: {quotient_fraction}")
