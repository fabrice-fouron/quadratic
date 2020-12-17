import math

class SecondDegree:
    """Second Degree equation module."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.quadratic_formula1 = (-1 * (self.b) + math.sqrt(abs(self.b**2 - (4 * self.a * self.c))))/(2 * self.a)
        self.quadratic_formula2 = (-1 * (self.b) - math.sqrt(abs(self.b**2 - (4 * self.a * self.c))))/(2 * self.a)

    def __str__(self):
        return f'{self.a}x**2 + {self.b}x + {self.c}'

    def has_factor(self):
        factors = set()
        fact = 1  # Loop factor
        while fact >= self.a * self.c:
            if fact + ((self.a * self.c)/fact) == self.b:
                factors.add(fact, (self.a * self.c)/fact)
            fact += 1

    def solve(self):
        if self.quadratic_formula1 == self.quadratic_formula2:
            return self.quadratic_formula1
        else:
            return (self.quadratic_formula1, self.quadratic_formula2)

