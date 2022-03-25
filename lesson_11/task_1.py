import time


class DateInitError(Exception):
    pass


class Date:
    def __init__(self, date):
        self.date = str(date)
        a, b, c = (Date.extract(self.date))
        try:
            if Date.valid(self.date):
                print(f'{str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}'
                      f' \nДата: {self.date}, результат: дата введена правильно')
        except DateInitError:
            print(f'{str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}'
                  f' \nДата: {self.date}, результат: дата введена неправильно')

    def __str__(self):
        a, b, c = (Date.extract(self.date))
        return f'{str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}'

    @classmethod
    def extract(cls, date):
        a, b, c = date.split('-')
        return int(a), int(b), int(c)

    @staticmethod
    def valid(date):
        try:
            time.strptime(date, '%d-%m-%Y')
            return True
        except Exception as exc:
            raise DateInitError()


c1 = Date('11-03-1899')
c2 = Date('12-13-1899')
