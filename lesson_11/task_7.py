class Complex:
    def __init__(self, real, imag=0):
        self.complex = complex(real, imag)

    def __str__(self):
        return self.complex.__str__()

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.complex

        complex = self.complex + other
        return Complex(complex.real, int(complex.imag))

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.complex

        complex = self.complex * other
        return Complex(complex.real, int(complex.imag))

c1 = Complex(5, 4)
c2 = Complex(-2, 3)
print(c1, c2)
print(c1 + c2)
print(c1 * c2)










