
class Storage:
    def __init__(self):
        self._data = {}

    def reception(self, *vendor_codes):
        for code in vendor_codes:
            if self._data.get(code):
                self._data[code] += 1
            else:
                self._data[code] = 1

        print(f'Товары с артикулами {vendor_codes} были приняты на склад.'
              f'\n\nТекущее количество товаров на складе: {self._data}')

    def transfer(self, *vendor_codes):
        for code in vendor_codes:
            if self._data.get(code) and self._data[code] > 0:
                self._data[code] -= 1
        print(f'\n\nТовары с артикулами {vendor_codes} были переданы в подразделения кампании.'
              f'Текущее количество переданных товаров : {self._data}')


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
        return f'{super.__str__(self)}' \
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
c4 = Printer('Canon', 'x100', '12423', '400')
print(c4)

storage.reception(c1, c2, c3, c1)
storage.transfer(c1)




