class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        return f' Площадь асфальта: {self._length * self._width}.'

class mass_of_asphalt(Road):
    def __init__(self, _length, _width, mass_of_meter):
        super().__init__(_length, _width)
        self.mass_of_meter = mass_of_meter

    def count(self):
        return f'Масса асфальта,' \
               f' необходимого для покрытия всей дороги ' \
               f'{self._length * self._width * self.mass_of_meter}'
        #mass_of_meter - масса асфальта для покрытия одного кв.
        # метра дороги асфальтом, толщиной в 1 см * число см
        # толщины полотна (25*5 = 125);


c1 = mass_of_asphalt(25,1000, 125)
print(c1.square())
print(c1.count())

c2 = mass_of_asphalt(35,1000, 125)
print(c2.square())
print(c2.count())