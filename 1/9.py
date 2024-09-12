from math import gcd


class Frac:
    numerator = 0
    denominator = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        GCD = gcd(numerator,denominator)
        self.numerator //= GCD
        self.denominator //= GCD
    
    def __add__(self, other):
        if isinstance(other, Frac):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Frac(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self + Frac(other, 1)
    
    def inverse(self):
        if self.numerator == 0:
            raise ValueError("Нельзя обратить дробь с нулевым числителем")
        return Frac(self.denominator, self.numerator)
    
    def __mul__(self, other):
        if isinstance(other, Frac):
            NewNumerator = self.numerator * other.denominator
            NewDenominator = self.denominator * other.denominator
            return Frac(NewNumerator, NewDenominator)
        elif isinstance(other, int):
            return self * Frac(other, 1)
    
    def __str__(self) -> str:
        return str(self.numerator) + "/" + str(self.denominator)
    

frac1 = Frac(1, 2)
frac2 = Frac(2, 4)

sum_frac = frac1 + frac2
print("Сумма дробей: ", sum_frac)

product_frac = frac1 * frac2
print("Произведение дробей: ", product_frac)

inverse_frac = frac1.inverse()
print("Обращение дроби: ", inverse_frac) 