class Storage:
    def __init__(self, name):
        self.name = name
        self.dicts = {}
    def reception(self):
        if self.dicts.get(self.name):
            self.dicts[self.name] += 1
        else:
            self.dicts[self.name] = 1
        print(f' Товар {self.name} был принят на склад.'
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

    def __str__(self,):
        return f'{Office_equipment.__str__(self)}\n Разрешение сканера:' \
               f'{self.permission}'

class Copier(Office_equipment):
    def __init__(self, name, model, color, scaling):
        super().__init__(name, model, color)
        self.scaling = scaling

    def __str__(self,):
        return f'{Office_equipment.__str__(self)}\n Масштабирование ксерокса:' \
               f'{self.scaling}'

c1 = Printer('Canon', 'x100', 'red', '400')
print(c1)
c2 = Scanner('Nikon', 'x200', 'black', '1000')
print(c2)
c3 = Copier('Xiomi', 'x500', 'white', 'yes')
print(c3)

c4 = Storage('Samsung')
c4.reception()
c5 = Storage('Siemens')
c5.reception()

