from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return str(self.value)

class Coat(Clothes):
    @property
    def consumption(self):
        return self.value / 6.5 + 0.5

class Suit(Clothes):
    @property
    def consumption(self):
        return self.value * 2 + 0.3

c1 = Coat(30)
c2 = Suit(1.7)
print(c1)
print(c1.consumption)
print(c2.consumption)


