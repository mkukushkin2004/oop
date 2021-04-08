# а теперь контроль над получением атрибутов, продолжение балета


class Point:
    WIDTH = 100

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __getattr__(self, item):  # вызывает только тогда, когда запрашиваем несуществующий атрибут
        # сначала всегда вызывается __getattribute__, если он кидает исключение - его перехватывает __getattr__
        print("Я поймал ошибку!")
        self.__dict__[item] = 0  # заметьте, что здесь мы спокойно используем __dict__, не боясь рекурсии
        return 0

    def __getattribute__(self, item):  # вызывает каждый раз при попытке взять атрибут, есть он или нет
        if item == "color":
            raise AttributeError("Цвет узнавать нельзя!")
        else:
            print('Возвращаю атрибут')
            return object.__getattribute__(self, item)


pt = Point(1, 2, 'red')
print(pt.z)

# все эти штуки называются "перегруженные методы" (мы их перегрузили)
