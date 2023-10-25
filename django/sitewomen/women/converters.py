class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


# для проверки частей кода при ответах на Stepic
# def info_salary(salary):
#     match salary:
#         case int() as s if s < 25000:
#             return "низкая"
#         case int() as s if 25000 <= s < 55000:
#             return "средняя"
#         case _:
#             return "высокая"

# if __name__ == '__main__':
#     print(info_salary(55_000))
#
#     req = {'a': 1, 'b': 2, 'c': 3}
#     print('|'.join([f'{k}={v}' for k, v in req.items()]))
