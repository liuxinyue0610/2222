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
    
    def __mul__(self, other):
        real_part = self.a * other.a - self.b * other.b
        imaginary_part = self.a * other.b + self.b * other.a
        return Complex(real_part, imaginary_part)

A = Complex(1, 2)
B = Complex(3, 4)
print(A)
print(B)

print(A+B)
print(A-B)
print(A*B)