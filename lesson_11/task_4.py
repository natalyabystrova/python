class Storage:
    def __init__(self):
        self.data = {}

    def reception(self, *equipment, n):
        for e in equipment:
            if self.data.get(e):
                self.data[e] += n
            else:
                self.data[e] = n
        for key, value in self.data.items():
            print(f'ТОВАР {key} \nБЫЛ ПРИНЯТ НА СКЛАД.'
                  f'\n\nТекущее количество данного товара на складе: {value} штук(а)')

    def transfer(self, *equipment, n):
        if type(n) == int:
            for e in equipment:
                for key, value in self.data.items():
                    if self.data.get(e) and self.data[e] > 0:
                        self.data[e] -= n
                        print(f'\n\nТовар {key} был передан в подразделения кампании.\n'
                        f'Текущее количество данного товара на складе: {value} штук(а)(и)')
                    else:
                        print(f'К сожалению, данный товар отсутствуют на складе в неободимом количестве.'
                              f'Текущее количество данного товара на складе: {value} штук(а)(и)')
        else:
            print("Ошибка! Второй аргумент должен быть числом!")


class OfficeEquipment:
    def __init__(self, name, model, vendor_codes):
        self.name = name
        self.model = model
        self.vendor_codes = vendor_codes

    def __repr__(self):
        return f'\nНазвание оборудования: {self.name}' \
               f'\nМодель: {self.model}' \
               f'\nАртикул: {self.vendor_codes}'


class Printer(OfficeEquipment):
    def __init__(self, name, model, vendor_codes, print_speed):
        super().__init__(name, model, vendor_codes)
        self.print_speed = print_speed

    def __str__(self):
        return f'{super.__str__(self)}\n' \
               f'Скорость принтера: {self.print_speed}'


class Scanner(OfficeEquipment):
    def __init__(self, name, model, vendor_codes, permission):
        super().__init__(name, model, vendor_codes)
        self.permission = permission

    def __str__(self):
        return f'{super.__str__(self)}' \
               f'Разрешение сканера: {self.permission}'


class Copier(OfficeEquipment):
    def __init__(self, name, model, vendor_codes, scaling):
        super().__init__(name, model, vendor_codes)
        self.scaling = scaling

    def __str__(self):
        return f'{super.__str__(self)}' \
               f'Масштабирование ксерокса: {self.scaling}'


storage = Storage()

c1 = Printer('Canon', 'x100', '12423', '400')
print(c1)
c2 = Scanner('Nikon', 'x200', '7656', '1000')
print(c2)
c3 = Copier('Xiomi', 'x500', '47647', 'yes')
print(c3)

storage.reception(c1, n=3)
storage.transfer(c1, n=1)

storage.transfer(c1, n=1)
storage.transfer(c1, n="jkbl")



