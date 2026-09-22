from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0, 1)
        i = 0
        n = len(expression)

        while i < n:
            j = i + 1

            while j < n and expression[j] not in "+-":
                j += 1

            result += Fraction(expression[i:j])
            i = j

        return f"{result.numerator}/{result.denominator}"