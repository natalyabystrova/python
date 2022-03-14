class Storage:
    def __init__(self, name):
        self.name = name
        self.dicts = {}

    def reception(self, equipment):
        if equipment in

class Office_equipment:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

class Printer(Office_equipment):
    def __init__(self, name, model, color, print_speed):
        super().__init__(name, model, color)
        self.print_speed = print_speed

class Scanner(Office_equipment):
    def __init__(self, name, model, color, permission):
        super().__init__(name, model, color)
        self.permission = permission

class Copier(Office_equipment):
    def __init__(self, name, model, color, scaling):
        super().__init__(name, model, color)
        self.scaling = scaling