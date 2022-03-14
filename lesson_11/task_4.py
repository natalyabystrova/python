class Storage:
    def __init__(self, name):
        self.name = name
        self.dicts = {}

    def reception(self, equipment):
        if self.dicts.get(equipment):
            self.dicts[equipment] += 1
        else:
            self.dicts[equipment] = 1
        print(f' Товар {equipment} был принят на склад.'
              f' Текущее количество товаров на складе: {self.dicts}')

class Office_equipment:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def __str__(self,):
        return f'Название оборудования: {self.name} \n Модель:' \
               f'{self.model} \n Цвет : {self.color}'

class Printer(Office_equipment):
    def __init__(self, name, model, color, print_speed):
        super().__init__(name, model, color)
        self.print_speed = print_speed

    def __str__(self,):
        return f'{Office_equipment.__str__(self)}\n Скорость принтера:' \
               f'{self.print_speed}'
class Scanner(Office_equipment):
    def __init__(self, name, model, color, permission):
        super().__init__(name, model, color)
        self.permission = permission

class Copier(Office_equipment):
    def __init__(self, name, model, color, scaling):
        super().__init__(name, model, color)
        self.scaling = scaling

c1 = Printer(Canon, x100, red, 400)