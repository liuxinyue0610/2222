class Complex:
    def __init__(self, real_part, imaginary_part):
        self.a = real_part
        self.b = imaginary_part

    def __str__(self):
        if self.b >= 0:
            return f"{self.a}+{self.b}i"
        else:
            return f"{self.a}{self.b}i"

    def __add__(self, other):
        real_part = self.a + other.a
        imaginary_part = self.b + other.b
        return Complex(real_part, imaginary_part)

    def __sub__(self, other):
        real_part = self.a - other.a
        imaginary_part = self.b - other.b
        return Complex(real_part, imaginary_part)

    def __neg__(self):
        return Complex(-self.a, -self.b)
    
    def __mul__(self, other):
        real_part = self.a * other.a - self.b * other.b
        imaginary_part = self.a * other.b + self.b * other.a
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        denominator = other.a**2 + other.b**2
        real_part = (self.a * other.a + self.b * other.b) / denominator
        imaginary_part = (self.b * other.a - self.a * other.b) / denominator
        return Complex(real_part, imaginary_part)


A = Complex(1, 2)
B = Complex(3, 4)

sum_result = A + B
difference_result = A - B
product_result = A * B

print("sum:", sum_result)
print("difference:", difference_result)
print("product:", product_result)