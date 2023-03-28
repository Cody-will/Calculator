# Joins together the numbers and operators, so they can be calculated using eval.
class Joiner:

    @classmethod
    def the_joining(cls, a, b, op):
        a = str(a)
        b = str(b)
        op = str(op)
        return str(a + op + b)

# For adding commas at the thousands place to show on screen or remove them for calculations
class Commas:
    @classmethod
    def remove(cls, number):
        return number.replace(',', '')

    @classmethod
    def add(cls, num):
        num = int(num)
        return str(f'{num:,}')

