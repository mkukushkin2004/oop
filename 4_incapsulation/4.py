# Теперь хотим получить контроль над удалением атрибутов


class Point:
    WIDTH = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):  # автоматически вызывается при удалении атрибута
        if item in self.__dict__.keys():  # если атрибут есть
            del self.__dict__[item]  # удаляем его
            print("Атрибут удалён")
        else:  # а тут мы избегаем ошибки, которая могла бы выскочить и прописываем нужное нам поведение
            print("Такого атрибута нет! Нечего удалять!")


pt = Point(5, 6)

del pt.x  # сработает __delattr__
print(pt.__dict__)

delattr(pt, 'z')  # тоже сработает __delattr__
delattr(Point, 'WIDTH')  # опа, а тут не сработает!

