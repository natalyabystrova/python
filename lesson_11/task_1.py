class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        res = date.split('-')
        return int(res[0]), int(res[1]), int(res[2])

    @staticmethod
    def valid(date):
        if Date.extract(date)[0] not in range(1, 32):
            return f'Дата введена неправильно: день должен быть в интервале 1-31.'
        elif Date.extract(date)[1] not in range(1, 13):
            return f'Дата введена неправильно: месяц должен быть в интервале 1-12.'
        elif Date.extract(date)[2] not in range(1900, 2023):
            return f'Дата введена неправильно: год должен быть в интервале 1900-2022.'
        else:
            return f'Дата введена правильно.'


    def __str__(self):
        return f'Введенная дата : {self.date}'


c1 = Date('14-03-2022')
print(c1)
print(Date.extract('12-03-2022'))
print(Date.valid('12-12-2000'))
print(Date.valid('32-12-2000'))
print(Date.valid('12-00-2000'))
print(Date.valid('12-12-2025'))

