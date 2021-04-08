# а теперь контроль над получением атрибутов


class Point:
    WIDTH = 100

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __getattribute__(self, item):  # вызывает каждый раз при попытке взять атрибут, есть он или нет
        if item == "color":
            raise AttributeError("Цвет узнавать нельзя!")
        else:
            print('Возвращаю атрибут')
            return object.__getattribute__(self, item)  # обращаемся таким образом, чтобы не попасть в рекурсию
            # здесь мы используем так называемый "базовый класс" object - родоначальник всех классов, высшая ступень


pt = Point(1, 2, 'red')
print(pt.x)  # работает __getattribute__
print(getattr(pt, 'y'))  # тоже работает
print(pt.WIDTH)  # тоже работает
print(Point.WIDTH)  # опа, а тут не работает!

print(pt.color)  # а здесь работает ошибочка!
