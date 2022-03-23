import time
class Date:
    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        a, b, c = (Date.extract(self.date))
        if Date.valid(self.date):
            return f' {str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}' \
                   f' \nДата {self.date}, результат: дата введена правильно!'

        else:
            return f' {str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}' \
                   f' \nДата {self.date}, результат: дата введена неправильно!'

    @classmethod
    def extract(cls, date):
        res = date.split('-')
        return int(res[0]), int(res[1]), int(res[2])

    @staticmethod
    def valid(date):
        try:
            valid_date = time.strptime(date, '%d-%m-%Y')
        except ValueError:
            return False
        else:
            return True

c1 = Date('11-03-1899')
print(c1)
c2 = Date('12-13-1899')
print(c2)


# import time
# class Date:
#     def __init__(self, date):
#         self.date = date
#         for d in self.date:
#             d = str(d)
#
#     # def __str__(self):
#     #     a, b, c = (Date.extract(self.date))
#     #     if Date.valid(self.date):
#     #         return f' {str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}' \
#     #                f' \nДата {self.date}, результат: дата введена правильно!'
#     #
#     #     else:
#     #         return f' {str(c)}.{str(b).zfill(2)}.{str(a).zfill(2)}' \
#     #                f' \nДата {self.date}, результат: дата введена неправильно!'
#     #
#     @classmethod
#     def extract(cls, date):
#         for d in date:
#             res = d.split('-')
#             return int(res[0]), int(res[1]), int(res[2])
#     #
#     # @staticmethod
#     # def valid(date):
#     #     try:
#     #         valid_date = time.strptime(date, '%d-%m-%Y')
#     #     except ValueError:
#     #         return False
#     #     else:
#     #         return True
#
# c1 = Date(['11-03-1891', '11-13.1892'])
# print(c1)
# print(Date.extract(c1))
#






