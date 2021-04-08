# создание для внутренних нужд статического метода и способ обращения к нему


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x  # private attribute (приватный атрибут)
        self.__y = y  # теперь доступ к нему - только через специальный метод

    @staticmethod
    def __check_value(x):  # приватный метод
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def set_coords(self, x, y):  # setter (сеттер)
        if Point.__check_value(x) and Point.__check_value(y):  # использование приватного метода
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
