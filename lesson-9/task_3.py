class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)



    def get_full_name(self):
        return f'{self.name} {self.surname}'


    def get_total_income(self):
        return f'{sum(self._income.values())}'

c1 = Position("Ivan", "Ivanov", "chef", 120000, 50000)
print(c1.get_full_name())
print(c1.get_total_income())


