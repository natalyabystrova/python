class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        result = f' Запуск отрисовки. Вы взяли {self.title}.'
        return result

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' Запуск отрисовки. Рисуем ручкой.'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return ' Запуск отрисовки. Рисуем карандашом.'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' Запуск отрисовки. Рисуем маркером.'

c1 = Handle("маркер")
c2 = Pencil("карандаш")
c3 = Pen("ручка")
print(c2.draw())


