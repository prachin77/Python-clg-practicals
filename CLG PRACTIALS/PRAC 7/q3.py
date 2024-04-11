class ComplexNumber:
    def __init__(self, real, imaginary=3):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def sub(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def mul(self, other):
        if other.real == 0 and other.imaginary == 0:
            raise ValueError("Cannot multiply by zero complex number")
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

# Example usage:
c1 = ComplexNumber(2)
c2 = ComplexNumber(1, 2)

print("c1:", c1)
print("c2:", c2)

add_result = c1.add(c2)
print("Addition result:", add_result)

sub_result = c1.sub(c2)
print("Subtraction result:", sub_result)

try:
    mul_result = c1.mul(c2)
    print("Multiplication result:", mul_result)
except ValueError as e:
    print("Error:", e)
