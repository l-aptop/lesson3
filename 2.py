import random


class Hide:
    __slots__ = "result"

    def __init__(self, num: int, num2: int):
        self.__hide(num, num2)
        del num, num2

    def __hide(self, num, num2):
        self.result = eval(f"{num}{random.choice(('-', '+', '*', '/', '%', '**', '//'))}{num2}")
        del num, num2

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return str(self)


hidden = Hide(2, 4)
print(hidden)
