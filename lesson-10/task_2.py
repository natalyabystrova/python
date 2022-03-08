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


lst = [Coat(30), Suit(1.7), Suit(1.6), Coat(20)]
result = {}
for i in lst:
    t = type(i)
    if result.get(t):
        result[t] += i.consumption
    else:
        result[t] = i.consumption
print(result)



