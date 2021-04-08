# аналогичная ситуация, только через декораторы


class Point:
    def __init__(self, x=0):
        self.__x = x

    @property
    def x(self):
        print("Получение свойства")
        return self.__x

    @x.setter
    def x(self, value):
        print("Установка свойства")
        self.__x = value

    @x.deleter
    def x(self):
        print("Удаление свойства")
        del self.__x


pt = Point()
print(pt.x)
pt.x = 5
print(pt.x)
del pt.x
