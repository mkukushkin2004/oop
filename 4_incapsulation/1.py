# приватные атрибуты объектов, нужны (например) для проверки корректности, доступ через сеттеры и геттеры


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x  # private attribute (приватный атрибут)
        self.__y = y  # теперь доступ к нему - только через специальный метод

    def set_coords(self, x, y):  # setter (сеттер)
        if (isinstance(x, int) or isinstance(x, float)) and \
                (isinstance(y, int) or isinstance(x, float)):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def get_coords(self):  # getter (геттер)
        return self.__x, self.__y


pt = Point(1, 2)
print(pt.get_coords())
pt.set_coords(10, 'Hello')
print(pt.get_coords())
print(pt.__dict__)