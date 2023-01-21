class o_int:
    number = int()

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other, number):
        if other.number == 0:
            return self.number + number


a = o_int(1)
b = o_int(1)
print(a+5)






