class Complex:
    def __init__(self, real, imag):
        self.real = real  #действительная часть
        self.imag = imag  #мнимая часть

    def __str__(self):
        return f'{self.real}{self.imag:+}j'

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other
            imag_part = self.imag
            return Complex(real_part, imag_part)
        if isinstance(other, Complex):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag
            return Complex(real_part, imag_part)

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real - other
            imag_part = self.imag
            return Complex(real_part, imag_part)
        if isinstance(other, Complex):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag
            return Complex(real_part, imag_part)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            real_part = self.real * other
            imag_part = self.imag * other
            return Complex(real_part, imag_part)
        if isinstance(other, Complex):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.real * other.imag) + (self.imag * other.real)
            return Complex(real_part, imag_part)


a = Complex(2, 3)
b = Complex(-1, 1)
c = 3
print(f'Умножение: {a * b}')
print(f'Вычитание: {a - b}')
print(f'Cложение: {a + b}')
print(f'Cложение: {a + c}')


#c использованием встроенной функции:
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

    def __sub__(self, other):
        if isinstance(other, Complex):
            other = other.complex

        complex = self.complex - other
        return Complex(complex.real, int(complex.imag))

# c1 = Complex(2+3j)
# c2 = Complex(-1+1j)
# print(c1, c2)
# print(c1 + c2)
# print(c1 * c2)
# print(c1 - c2)






