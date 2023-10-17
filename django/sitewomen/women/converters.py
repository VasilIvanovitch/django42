class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


# для проверки частей кода при ответах на Stepic
# if __name__ == '__main__':
#
#     req = {'a': 1, 'b': 2, 'c': 3}
#     print('|'.join([f'{k}={v}' for k, v in req.items()]))
