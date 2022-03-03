class Car:
    name = None
    speed = None
    color = None
    is_police = False
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала!'

    def stop(self):
        return f'{self.name} остановилась!'

    def turn(self, direction):
        return f'{self.name} повернула {direction}!'

    def show_speed(self):
        return f'Текущая скорость {self.name}:{self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейской машиной!'
        else:
            return f'Автомобиль {self.name} не является полицейской машиной!'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч. Допустимая скорость превышена!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч. Допустимая скорость превышена!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

c1 = WorkCar(70,'Красная', 'Ауди', False)
print(c1.go())
print(c1.show_speed())
print(c1.stop())
print(c1.turn("направо"))
print(c1.show_speed())

c2 = TownCar(70, 'черная', 'бмв', False)
print(c2.show_speed())
print(c2.police())

c3 = PoliceCar(100, "белый", "Форд", True)
print(c3.police())

c4 = TownCar(40, 'черная', 'Ниссан', False)
print(c4.show_speed())