from time import sleep
from itertools import cycle


class TrafficLight:
    states = {'красный': 7, 'желтый': 2, 'зеленый': 7}
    _current_iterate = 0

    def __init__(self, repeat=1):
        self._max_iterate_count = repeat

    def running(self):
        data = list(self.states.items())
        data = data + data[1:-1]
        for color, timer in cycle(data):
            if self._current_iterate == self._max_iterate_count:
                break
            print(f"Светофор изменил сигнал на '{color}' на {timer} секунд")
            sleep(timer)
            if color == 'зеленый':
                self._current_iterate += 1


if __name__ == '__main__':
    c1 = TrafficLight(repeat=2)
    c1.running()
