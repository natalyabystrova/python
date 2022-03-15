class Complex_number:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __str__(self):
        return f'z = self.a + self.b * i'

    def __add__(self, other):
        return